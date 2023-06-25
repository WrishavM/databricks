# Databricks notebook source
remote_table = (spark.read
  .format("sqlserver")
  .option("host", "wrishavgo.database.windows.net")
 
  .option("user", "adminsql")
  .option("password", "Titu@143")
  .option("database", "client1")
  .option("dbtable", "dbo.name") # (if schemaName not provided, default to "dbo")
  .load()
)

# COMMAND ----------

remote_table.show()

# COMMAND ----------

remote_table.createOrReplaceTempView('table')
spark.sql("select * from table").show()

# COMMAND ----------


