# **🚀 BigQuery CSV Uploader**  

Easily upload multiple **CSV files** to **Google BigQuery**, ensuring seamless data integration with **automatic table creation, retry mechanisms, and detailed logging**. This tool is built for **data engineers, analysts, and developers** who need a **robust and scalable** solution for managing CSV imports into BigQuery.

---

## **🔥 Features**
✅ **Automated Table Creation** – No need to manually create tables; the script does it for you!  
✅ **Smart Retry Logic** – Retries failed uploads **up to 3 times** before marking them as failed.  
✅ **Seamless BigQuery Integration** – Uses the official **Google Cloud BigQuery API**.  
✅ **Detailed Logging** – Get clear insights into upload progress, errors, and success rates.  
✅ **Handles Large Datasets** – Supports bulk uploads efficiently.  

---

## **📌 How It Works**
1️⃣ Drop your **CSV files** into the script.  
2️⃣ It checks if the corresponding tables exist in **BigQuery**.  
3️⃣ If missing, it **creates the table** automatically.  
4️⃣ The script **uploads the data**, handling any errors or retries.  
5️⃣ Get a **summary of failed files** (if any).  

---

## **🔧 Setup & Usage**
```python
csv_files = {
    "sales_data.csv": open("sales_data.csv", "rb").read(),
    "customer_info.csv": open("customer_info.csv", "rb").read(),
}

failed_files = upload_csv_to_bigquery("your-project-id", "your-dataset-id", csv_files)

if failed_files is not None:
    print("Some files failed to upload:", failed_files)
else:
    print("All files uploaded successfully! 🚀")
```

---

## **📦 Why Use This?**
- 🏎 **Fast & Efficient** – Optimized for **high-performance bulk uploads**.  
- 🛠 **No Manual Work** – Tables are **auto-created** and **autodetected**.  
- 🔄 **Safe & Reliable** – **Retries failures** to ensure **data integrity**.  

An **ETL pipelines, data warehousing, and real-time analytics** to streamline your **BigQuery CSV uploads**.
