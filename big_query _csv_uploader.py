import io
import pandas as pd
from google.cloud import bigquery
from google.cloud.exceptions import NotFound

def upload_csv_to_bigquery(project_id, dataset_id, csv_files, max_retries=3):
    """
    Uploads multiple CSV files to Google BigQuery, creating tables if they do not exist.

    Args:
        project_id (str): Google Cloud Project ID.
        dataset_id (str): BigQuery dataset ID.
        csv_files (dict): Dictionary where keys are filenames and values are file contents (bytes).
        max_retries (int): Maximum number of retries for failed uploads.

    Returns:
        pd.DataFrame: DataFrame listing files that failed to upload.
    """
    client = bigquery.Client(project=project_id)
    dataset_ref = client.dataset(dataset_id)
    failed_files = []

    for filename, file_content in csv_files.items():
        if filename.endswith(".csv"):
            table_name = filename.rsplit('.', 1)[0]
            table_ref = dataset_ref.table(table_name)
            job_config = bigquery.LoadJobConfig(
                source_format=bigquery.SourceFormat.CSV,
                autodetect=True,
            )

            file_obj = io.BytesIO(file_content)
            file_obj.seek(0)  # Ensure file pointer is at the start

            for attempt in range(max_retries):
                try:
                    # Check if table exists
                    try:
                        client.get_table(table_ref)  # Will raise NotFound if the table does not exist
                        print(f"Table '{table_name}' already exists.")
                    except NotFound:
                        print(f"Table '{table_name}' not found. Creating and uploading data...")

                    # Upload the CSV file to BigQuery
                    job = client.load_table_from_file(file_obj, table_ref, job_config=job_config)
                    job.result()  # Wait for the job to complete

                    print(f"✅ Successfully loaded {job.output_rows} rows into {dataset_id}.{table_name}")
                    break  # Exit retry loop on success

                except Exception as e:
                    print(f"❌ Failed to upload {filename}: {e}")
                    if attempt == max_retries - 1:
                        print(f"🚨 Max retries reached for {filename}. Adding to failed list.")
                        failed_files.append(filename)
                    else:
                        print(f"🔄 Retrying {filename}... Attempt {attempt + 2}/{max_retries}")

    # Return a DataFrame listing files that failed to upload
    return pd.DataFrame(failed_files, columns=['Failed Files']) if failed_files else None
