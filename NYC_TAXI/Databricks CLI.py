# Databricks notebook source
# MAGIC %md
# MAGIC ## This notebook is used to explore the NYC taxi dataset

# COMMAND ----------

# MAGIC %md
# MAGIC #### Databricks command line tool (CLI)
# MAGIC
# MAGIC Databricks CLI can be used from local machine or directly from cluster. I used the terminal that is available from the cluster (min version LTS 15) to execute the following commands.
# MAGIC
# MAGIC # 
# MAGIC
# MAGIC ```bash
# MAGIC root@0204-110140-shecuwop-10-147-237-10:~# databricks -h
# MAGIC Installing the CLI...
# MAGIC Installed Databricks CLI v0.215.0 at /root/bin/databricks.
# MAGIC Databricks CLI
# MAGIC
# MAGIC Usage:
# MAGIC   databricks [command]
# MAGIC
# MAGIC Databricks Workspace
# MAGIC   fs                      Filesystem related commands
# MAGIC   git-credentials         Registers personal access token for Databricks to do operations on behalf of the user.
# MAGIC   repos                   The Repos API allows users to manage their git repos.
# MAGIC   secrets                 The Secrets API allows you to manage secrets, secret scopes, and access permissions.
# MAGIC   workspace               The Workspace API allows you to list, import, export, and delete notebooks and folders.
# MAGIC
# MAGIC Compute
# MAGIC   cluster-policies        You can use cluster policies to control users' ability to configure clusters based on a set of rules.
# MAGIC   clusters                The Clusters API allows you to create, start, edit, list, terminate, and delete clusters.
# MAGIC   global-init-scripts     The Global Init Scripts API enables Workspace administrators to configure global initialization scripts for their workspace.
# MAGIC   instance-pools          Instance Pools API are used to create, edit, delete and list instance pools by using ready-to-use cloud instances which reduces a cluster start and auto-scaling times.
# MAGIC   instance-profiles       The Instance Profiles API allows admins to add, list, and remove instance profiles that users can launch clusters with.
# MAGIC   libraries               The Libraries API allows you to install and uninstall libraries and get the status of libraries on a cluster.
# MAGIC   policy-families         View available policy families.
# MAGIC   ```

# COMMAND ----------

# MAGIC %md
# MAGIC ### Databricks CLI filesystem commands
# MAGIC
# MAGIC #
# MAGIC
# MAGIC ```bash
# MAGIC root@0204-110140-shecuwop-10-147-237-10:~# databricks fs -h
# MAGIC Commands to do file system operations on DBFS and UC Volumes.
# MAGIC
# MAGIC Usage:
# MAGIC   databricks fs [command]
# MAGIC
# MAGIC Available Commands:
# MAGIC   cat         Show file content.
# MAGIC   cp          Copy files and directories.
# MAGIC   ls          Lists files.
# MAGIC   mkdir       Make directories.
# MAGIC   rm          Remove files and directories.
# MAGIC
# MAGIC Flags:
# MAGIC   -h, --help   help for fs
# MAGIC
# MAGIC Global Flags:
# MAGIC       --debug            enable debug logging
# MAGIC   -o, --output type      output type: text or json (default text)
# MAGIC   -p, --profile string   ~/.databrickscfg profile
# MAGIC   -t, --target string    bundle target to use (if applicable)
# MAGIC ```

# COMMAND ----------

# MAGIC %md
# MAGIC ### Create user folder using databricks CLI
# MAGIC
# MAGIC Databricks CLI can be used to create folders in dbfs (databricks file system).
# MAGIC # 
# MAGIC
# MAGIC ```bash
# MAGIC databricks fs mkdir  dbfs:/user/basus
# MAGIC ```

# COMMAND ----------

# MAGIC %md
# MAGIC
