{
    "metadata": {
        "kernelspec": {
            "name": "SQL",
            "display_name": "SQL",
            "language": "sql"
        },
        "language_info": {
            "name": "sql",
            "version": ""
        }
    },
    "nbformat_minor": 2,
    "nbformat": 4,
    "cells": [
        {
            "cell_type": "markdown",
            "source": [
                "# Data Cleaning with SQL\r\n",
                "\r\n",
                "First, let's take a look on the Starbucks dataset: "
            ],
            "metadata": {
                "azdata_cell_guid": "ca023499-34a1-49c0-b5ba-af3b51543435",
                "language": ""
            },
            "attachments": {}
        },
        {
            "cell_type": "markdown",
            "source": [
                "```\n",
                "SELECT * FROM [dbo].['Starbucks satisfactory survey e$']\n",
                "```"
            ],
            "metadata": {
                "azdata_cell_guid": "74914717-43ba-4df0-8f2b-c845fe79b8b9"
            },
            "attachments": {}
        },
        {
            "cell_type": "markdown",
            "source": [
                "<span style=\"color: rgb(36, 41, 47); font-family: ui-monospace, SFMono-Regular, &quot;SF Mono&quot;, Menlo, Consolas, &quot;Liberation Mono&quot;, monospace; font-size: 12px; white-space: pre; background-color: rgb(255, 255, 255);\">The dataset contains 34 columns that it is encoded according to the answers provided on the survey.</span>\n",
                "\n",
                "<span style=\"color: rgb(36, 41, 47); font-family: ui-monospace, SFMono-Regular, &quot;SF Mono&quot;, Menlo, Consolas, &quot;Liberation Mono&quot;, monospace; font-size: 12px; white-space: pre; background-color: rgb(255, 255, 255);\">Here are the original labels for each column that I will use:</span><span style=\"color: rgb(36, 41, 47); font-family: ui-monospace, SFMono-Regular, &quot;SF Mono&quot;, Menlo, Consolas, &quot;Liberation Mono&quot;, monospace; font-size: 12px; white-space: pre; background-color: rgb(255, 255, 255);\"><br></span>"
            ],
            "metadata": {
                "azdata_cell_guid": "bfa9e671-2c66-4438-96a6-12699335328e"
            },
            "attachments": {}
        },
        {
            "cell_type": "markdown",
            "source": [
                "| gender      | age               | status            | income                    | VisitNo     | method         | timeSpend        | location          | membershipCard |\n",
                "|-------------|-------------------|-------------------|---------------------------|-------------|----------------|------------------|-------------------|----------------|\n",
                "| 0 = Male    | 0 = Below 20      | 0 = Student       | 0 = Less than RM25,000    | 0 = Daily   | 0 = Dine-In    | 0 = Below 30 min | 0 = Within 1 km   | 0 = Yes        |\n",
                "| 1 = Female  | 1 = From 20 - 29  | 1 = Self-Employed | 1 = RM25,000 - RM50,000   | 1 = Weekly  | 1 = Drive-thru | 1 = 30 min - 1h  | 1 = 1km - 2km     | 1 = No         |\n",
                "|             | 2 = From 30 to 39 | 2 = Employed      | 2 = RM50,000 - RM100,000  | 3 = Monthly | 2 = Take away  | 2 = 1h - 2h      | 3 = More than 3km |                |\n",
                "|             | 3 = 40 and above  | 3 = Housewife     | 3 = RM100,000 - RM150,000 | 4 = Never   | 3 = Never      | 3 = 2h - 3h      |                   |                |\n",
                "|             |                   |                   | 4 = More than RM150,000   |             | 4 = Others     | 4 = More than 3h |                   |                |"
            ],
            "metadata": {
                "azdata_cell_guid": "a470bcbf-67bd-43c7-a97d-8f5cbd7e301a"
            },
            "attachments": {}
        },
        {
            "cell_type": "markdown",
            "source": [
                "<span style=\"color: rgb(36, 41, 47); font-family: ui-monospace, SFMono-Regular, &quot;SF Mono&quot;, Menlo, Consolas, &quot;Liberation Mono&quot;, monospace; font-size: 12px; white-space: pre; background-color: rgb(255, 255, 255);\">To clean this dataset, it will be needed to first convert the columns that have integer type into varchar (string). </span> <span style=\"background-color: rgb(255, 255, 255); color: rgb(36, 41, 47); font-family: ui-monospace, SFMono-Regular, &quot;SF Mono&quot;, Menlo, Consolas, &quot;Liberation Mono&quot;, monospace; font-size: 12px; white-space: pre;\">Then, update each value to match the labels above.</span>\n",
                "\n",
                "<span style=\"color: rgb(36, 41, 47); font-family: ui-monospace, SFMono-Regular, &quot;SF Mono&quot;, Menlo, Consolas, &quot;Liberation Mono&quot;, monospace; font-size: 12px; white-space: pre; background-color: rgb(255, 255, 255);\">--Checking data type on gender column.</span><span style=\"background-color: rgb(255, 255, 255); color: rgb(36, 41, 47); font-family: ui-monospace, SFMono-Regular, &quot;SF Mono&quot;, Menlo, Consolas, &quot;Liberation Mono&quot;, monospace; font-size: 12px; white-space: pre;\"><br></span>"
            ],
            "metadata": {
                "azdata_cell_guid": "7c3bf698-4d7c-402c-b728-fba0fc072955"
            },
            "attachments": {}
        },
        {
            "cell_type": "markdown",
            "source": [
                "```\n",
                "SELECT DATA_TYPE \n",
                "FROM INFORMATION_SCHEMA.COLUMNS\n",
                "WHERE COLUMN_NAME = 'gender'\n",
                "\n",
                "```"
            ],
            "metadata": {
                "azdata_cell_guid": "d5164f43-dc42-4412-899b-4667e1c6d6b6"
            },
            "attachments": {}
        },
        {
            "cell_type": "markdown",
            "source": [
                "<span style=\"color: rgb(36, 41, 47); font-family: ui-monospace, SFMono-Regular, &quot;SF Mono&quot;, Menlo, Consolas, &quot;Liberation Mono&quot;, monospace; font-size: 12px; white-space: pre; background-color: rgb(255, 255, 255);\">-- Altering data type from float to varchar.</span>\n",
                "\n",
                "```\n",
                "ALTER TABLE [dbo].['Starbucks satisfactory survey e$'] \n",
                "ALTER COLUMN gender varchar(10)\n",
                "\n",
                "```"
            ],
            "metadata": {
                "azdata_cell_guid": "5be83e22-e691-4691-a33c-bf13cf7420c4"
            },
            "attachments": {}
        },
        {
            "cell_type": "markdown",
            "source": [
                "<span style=\"color: rgb(36, 41, 47); font-family: ui-monospace, SFMono-Regular, &quot;SF Mono&quot;, Menlo, Consolas, &quot;Liberation Mono&quot;, monospace; font-size: 12px; white-space: pre; background-color: rgb(255, 255, 255);\">--Updating values of the column according to the labels provided</span>\n",
                "```\n",
                "UPDATE [dbo].['Starbucks satisfactory survey e$'] \n",
                "SET gender =  ( \n",
                "     CASE     \n",
                "            WHEN gender = 0  THEN 'Male'    \n",
                "            WHEN gender = 1  THEN 'Female'    \n",
                "            END )\n",
                "            WHERE gender = 0 or gender = 1\n",
                "```"
            ],
            "metadata": {
                "azdata_cell_guid": "0513bfc7-7bd1-43a6-a552-0b6d2dcfa8b9"
            },
            "attachments": {}
        },
        {
            "cell_type": "markdown",
            "source": [
                "<span style=\"color: rgb(36, 41, 47); font-family: ui-monospace, SFMono-Regular, &quot;SF Mono&quot;, Menlo, Consolas, &quot;Liberation Mono&quot;, monospace; font-size: 12px; white-space: pre; background-color: rgb(255, 255, 255);\">--Checking data type</span>\n",
                "```\n",
                "SELECT DATA_TYPE \n",
                "FROM INFORMATION_SCHEMA.COLUMNS\n",
                "WHERE COLUMN_NAME = 'age'   \n",
                "```"
            ],
            "metadata": {
                "azdata_cell_guid": "c1d3f53a-4fc6-4d80-986c-518313b82268"
            },
            "attachments": {}
        },
        {
            "cell_type": "markdown",
            "source": [
                "<span style=\"color: rgb(36, 41, 47); font-family: ui-monospace, SFMono-Regular, &quot;SF Mono&quot;, Menlo, Consolas, &quot;Liberation Mono&quot;, monospace; font-size: 12px; white-space: pre; background-color: rgb(255, 255, 255);\">--Altering data type</span>\n",
                "```\n",
                "ALTER TABLE [dbo].['Starbucks satisfactory survey e$']\n",
                "ALTER COLUMN age varchar(20)\n",
                "```"
            ],
            "metadata": {
                "azdata_cell_guid": "18a960c0-96f6-4f17-81df-750ac00eecc3"
            },
            "attachments": {}
        },
        {
            "cell_type": "markdown",
            "source": [
                "<span style=\"color: rgb(36, 41, 47); font-family: ui-monospace, SFMono-Regular, &quot;SF Mono&quot;, Menlo, Consolas, &quot;Liberation Mono&quot;, monospace; font-size: 12px; white-space: pre; background-color: rgb(255, 255, 255);\">--Updating values</span>\n",
                "```\n",
                "UPDATE [dbo].['Starbucks satisfactory survey e$'] \n",
                "SET age =(  \n",
                "    CASE     \n",
                "        WHEN age = 0 THEN 'Below 20'    \n",
                "        WHEN age = 1 THEN 'From 20 to 29'    \n",
                "        WHEN age = 2 THEN 'From 30 to 39'    \n",
                "        WHEN age = 3 THEN '40 and above'    \n",
                "        END )\n",
                "WHERE age IN (0,1,2,3)\n",
                "```"
            ],
            "metadata": {
                "azdata_cell_guid": "5366a5ee-cc49-4a02-a9da-431af5a103fb"
            },
            "attachments": {}
        },
        {
            "cell_type": "markdown",
            "source": [
                "<span style=\"color: rgb(36, 41, 47); font-family: ui-monospace, SFMono-Regular, &quot;SF Mono&quot;, Menlo, Consolas, &quot;Liberation Mono&quot;, monospace; font-size: 12px; white-space: pre; background-color: rgb(255, 255, 255);\">--Checking dataset</span>\n",
                "```\n",
                "SELECT *\n",
                "FROM [dbo].['Starbucks satisfactory survey e$']  \n",
                "```"
            ],
            "metadata": {
                "azdata_cell_guid": "0be8f1f4-4e7d-4c85-812b-81fb457fb435"
            },
            "attachments": {}
        },
        {
            "cell_type": "markdown",
            "source": [
                "<span style=\"color: rgb(36, 41, 47); font-family: ui-monospace, SFMono-Regular, &quot;SF Mono&quot;, Menlo, Consolas, &quot;Liberation Mono&quot;, monospace; font-size: 12px; white-space: pre; background-color: rgb(255, 255, 255);\">--Repeating the process for 'status' column</span>\n",
                "```\n",
                "ALTER TABLE [dbo].['Starbucks satisfactory survey e$'] \n",
                "ALTER COLUMN status varchar(20)\n",
                "\n",
                "UPDATE [dbo].['Starbucks satisfactory survey e$'] \n",
                "SET status = (\n",
                "    \tCASE\t\t\n",
                "            WHEN status = 0 THEN 'Student'\t\t\n",
                "            WHEN status = 1 THEN 'Self-Employed'\t\t\n",
                "            WHEN status = 2 THEN 'Employed'\t\t\n",
                "            WHEN status = 3 THEN 'Housewife'\t\t\n",
                "            END)\n",
                "WHERE status IN (0,1,2,3);    \n",
                "```"
            ],
            "metadata": {
                "azdata_cell_guid": "443c13d7-a7aa-40c2-b0d0-706858512f6b"
            },
            "attachments": {}
        },
        {
            "cell_type": "markdown",
            "source": [
                "<span style=\"color: rgb(36, 41, 47); font-family: ui-monospace, SFMono-Regular, &quot;SF Mono&quot;, Menlo, Consolas, &quot;Liberation Mono&quot;, monospace; font-size: 12px; white-space: pre; background-color: rgb(255, 255, 255);\">--Repeating the process for 'income' column</span>\n",
                "```\n",
                "ALTER TABLE [dbo].['Starbucks satisfactory survey e$']\n",
                "ALTER COLUMN income varchar(30)\n",
                "\n",
                "UPDATE [dbo].['Starbucks satisfactory survey e$'] \n",
                "SET income =(\t\n",
                "    CASE\t\t\n",
                "        WHEN income = 0 THEN 'Less than RM25,000 '\t\t\n",
                "        WHEN income = 1 THEN 'RM25,000 – RM50,000'\t\t\n",
                "        WHEN income = 2 THEN 'RM50,000 – RM100,000'\t\t\n",
                "        WHEN income = 3 THEN 'RM100,000 – RM150,000'\t\t\n",
                "        WHEN income = 4 THEN 'More than RM150,000'\t\t\n",
                "        END)\n",
                "WHERE income IN (0,1,2,3,4);   \n",
                "```"
            ],
            "metadata": {
                "azdata_cell_guid": "9cf15060-370a-4241-acc1-9830cdd5d0ce"
            },
            "attachments": {}
        },
        {
            "cell_type": "markdown",
            "source": [
                "<span style=\"background-color: rgb(255, 255, 255); color: rgb(36, 41, 47); font-family: ui-monospace, SFMono-Regular, &quot;SF Mono&quot;, Menlo, Consolas, &quot;Liberation Mono&quot;, monospace; font-size: 12px; white-space: pre;\">When updating the next column (visitNo), I noticed that it was missing a label for number 2</span>\n",
                "\n",
                "<span style=\"color: rgb(36, 41, 47); font-family: ui-monospace, SFMono-Regular, &quot;SF Mono&quot;, Menlo, Consolas, &quot;Liberation Mono&quot;, monospace; font-size: 12px; white-space: pre; background-color: rgb(255, 255, 255);\"><b>(</b></span><span style=\"background-color: rgb(255, 255, 255); color: rgb(36, 41, 47); font-family: ui-monospace, SFMono-Regular, &quot;SF Mono&quot;, Menlo, Consolas, &quot;Liberation Mono&quot;, monospace; font-size: 12px; white-space: pre;\"><b>0 - Daily, 1 - Weekly, 3 - Monthly, 4 - Rarely)</b>. </span>  \n",
                "\n",
                "<span style=\"background-color: rgb(255, 255, 255); color: rgb(36, 41, 47); font-family: ui-monospace, SFMono-Regular, &quot;SF Mono&quot;, Menlo, Consolas, &quot;Liberation Mono&quot;, monospace; font-size: 12px; white-space: pre;\">Some investigation was required.</span>\n",
                "\n",
                "<span style=\"color: rgb(36, 41, 47); font-family: ui-monospace, SFMono-Regular, &quot;SF Mono&quot;, Menlo, Consolas, &quot;Liberation Mono&quot;, monospace; font-size: 12px; white-space: pre; background-color: rgb(255, 255, 255);\">--I grouped the values to check how many values '2' were missing.</span><span style=\"background-color: rgb(255, 255, 255); color: rgb(36, 41, 47); font-family: ui-monospace, SFMono-Regular, &quot;SF Mono&quot;, Menlo, Consolas, &quot;Liberation Mono&quot;, monospace; font-size: 12px; white-space: pre;\"><br></span>\n",
                "\n",
                "```\n",
                "SELECT count(*), visitNo\n",
                "FROM [dbo].['Starbucks satisfactory survey e$']  \n",
                "GROUP BY visitNo\n",
                "\n",
                "```"
            ],
            "metadata": {
                "azdata_cell_guid": "9afcf53c-19c2-4a6b-b9a3-a3cdd0c598c3"
            },
            "attachments": {}
        },
        {
            "cell_type": "markdown",
            "source": [
                "<span style=\"background-color: rgb(255, 255, 255); color: rgb(36, 41, 47); font-family: ui-monospace, SFMono-Regular, &quot;SF Mono&quot;, Menlo, Consolas, &quot;Liberation Mono&quot;, monospace; font-size: 12px; white-space: pre;\">When grouping the values, I noticed that there were not any '4' values, and only the label for value '2' was missing.</span>\n",
                "\n",
                "<span style=\"color: rgb(36, 41, 47); font-family: ui-monospace, SFMono-Regular, &quot;SF Mono&quot;, Menlo, Consolas, &quot;Liberation Mono&quot;, monospace; font-size: 12px; white-space: pre; background-color: rgb(255, 255, 255);\">After checking further, the legend of this column was not correct, so I only need to correct the labels.</span>\n",
                "\n",
                "<span style=\"color: rgb(36, 41, 47); font-family: ui-monospace, SFMono-Regular, &quot;SF Mono&quot;, Menlo, Consolas, &quot;Liberation Mono&quot;, monospace; font-size: 12px; white-space: pre; background-color: rgb(255, 255, 255);\">--Altering data type</span><span style=\"color: rgb(36, 41, 47); font-family: ui-monospace, SFMono-Regular, &quot;SF Mono&quot;, Menlo, Consolas, &quot;Liberation Mono&quot;, monospace; font-size: 12px; white-space: pre; background-color: rgb(255, 255, 255);\"><br></span>\n",
                "\n",
                "```\n",
                "ALTER TABLE [dbo].['Starbucks satisfactory survey e$'] \n",
                "ALTER COLUMN visitNo varchar(10)\n",
                "\n",
                "```\n",
                "--Updating the values\n",
                "```\n",
                "UPDATE [dbo].['Starbucks satisfactory survey e$'] \n",
                "SET visitNo = (\t\n",
                "    CASE \t\t\n",
                "        WHEN visitNo = 0 THEN 'Daily'\t\t\n",
                "        WHEN visitNo = 1 THEN 'Weekly'\t\t\n",
                "        WHEN visitNo = 2 THEN 'Monthly'\t\t\n",
                "        WHEN visitNo = 3 THEN 'Rarely'\t\t\n",
                "        END)\t\n",
                "WHERE visitNo IN (0,1,2,3)   \n",
                "```"
            ],
            "metadata": {
                "azdata_cell_guid": "aa05b4b4-f3ef-45e6-9c51-1c8b38918043"
            },
            "attachments": {}
        },
        {
            "cell_type": "markdown",
            "source": [
                "<span style=\"color: rgb(36, 41, 47); font-family: ui-monospace, SFMono-Regular, &quot;SF Mono&quot;, Menlo, Consolas, &quot;Liberation Mono&quot;, monospace; font-size: 12px; white-space: pre; background-color: rgb(255, 255, 255);\">--Repeating the process for 'method' column</span>\n",
                "```\n",
                "ALTER TABLE [dbo].['Starbucks satisfactory survey e$'] \n",
                "ALTER COLUMN method varchar(15)\n",
                "\n",
                "UPDATE [dbo].['Starbucks satisfactory survey e$'] \n",
                "SET method = (\t\n",
                "    CASE \t\t\n",
                "    WHEN method = 0 THEN 'Dine in'\t\t\n",
                "    WHEN method = 1 THEN 'Drive-thru'\t\t\n",
                "    WHEN method = 2 THEN 'Take Away'\t\t\n",
                "    WHEN method = 3 THEN 'Never'\t\t\n",
                "    WHEN method = 4 THEN 'Others'\t\t\n",
                "    END)\t\n",
                "WHERE method IN (0,1,2,3) \n",
                "```"
            ],
            "metadata": {
                "azdata_cell_guid": "162c4a15-b076-4120-bd16-c71d3d7f9d0b"
            },
            "attachments": {}
        },
        {
            "cell_type": "markdown",
            "source": [
                "<span style=\"color: rgb(36, 41, 47); font-family: ui-monospace, SFMono-Regular, &quot;SF Mono&quot;, Menlo, Consolas, &quot;Liberation Mono&quot;, monospace; font-size: 12px; white-space: pre; background-color: rgb(255, 255, 255);\">I notice that the column values do not fully match with the labels provided for this survey.</span>\n",
                "\n",
                "**<span style=\"color: rgb(36, 41, 47); font-family: ui-monospace, SFMono-Regular, &quot;SF Mono&quot;, Menlo, Consolas, &quot;Liberation Mono&quot;, monospace; font-size: 12px; white-space: pre; background-color: rgb(255, 255, 255);\">(</span><span style=\"background-color: rgb(255, 255, 255); color: rgb(36, 41, 47); font-family: ui-monospace, SFMono-Regular, &quot;SF Mono&quot;, Menlo, Consolas, &quot;Liberation Mono&quot;, monospace; font-size: 12px; white-space: pre;\">0- Dine In, 1- Drive-thru, 2- Take away, 3- Never, 4- Others)</span>**\n",
                "\n",
                "```\n",
                "SELECT count(*), method\n",
                "FROM [dbo].['Starbucks satisfactory survey e$']  \n",
                "GROUP BY method \n",
                "\n",
                "```\n",
                "--After further investigation, there is one value of '5', and there is no value '3' or '4'.\n",
                "--I updated this value(5) as 3 and labeled it as 'Others'\n",
                "  \n",
                "--Updating value 5 to 3.\n",
                "```\n",
                "UPDATE [dbo].['Starbucks satisfactory survey e$'] \n",
                "SET method = 3\n",
                "WHERE method = 5;  \n",
                "```\n",
                "--Altering the data type.\n",
                "```\n",
                "ALTER TABLE [dbo].['Starbucks satisfactory survey e$'] \n",
                "ALTER COLUMN method varchar(15)\n",
                "```\n",
                "--Updating values.\n",
                "```\n",
                "UPDATE [dbo].['Starbucks satisfactory survey e$'] \n",
                "SET method = (\n",
                "\tCASE \n",
                "\t\tWHEN method = 0 THEN 'Dine in'\n",
                "\t\tWHEN method = 1 THEN 'Drive-thru'\n",
                "\t\tWHEN method = 2 THEN 'Take Away'\n",
                "\t\tWHEN method = 3 THEN 'Others'\n",
                "\t\tEND)\n",
                "\tWHERE method IN (0,1,2,3)\n",
                "```"
            ],
            "metadata": {
                "azdata_cell_guid": "318950e0-afea-4468-ab15-d661aa8c2bed"
            },
            "attachments": {}
        },
        {
            "cell_type": "markdown",
            "source": [
                "<span style=\"color: rgb(36, 41, 47); font-family: ui-monospace, SFMono-Regular, &quot;SF Mono&quot;, Menlo, Consolas, &quot;Liberation Mono&quot;, monospace; font-size: 12px; white-space: pre; background-color: rgb(255, 255, 255);\">--Repeating the process for 'timeSpend' column.</span>\r\n",
                "\r\n",
                "```\r\n",
                "ALTER TABLE [dbo].['Starbucks satisfactory survey e$'] \r\n",
                "ALTER COLUMN timeSpend varchar(20)\r\n",
                "\r\n",
                "UPDATE [dbo].['Starbucks satisfactory survey e$'] \r\n",
                "SET timeSpend = (\r\n",
                "\tCASE\r\n",
                "\t\tWHEN timeSpend = 0 THEN 'Below 30 minutes'\r\n",
                "\t\tWHEN timeSpend = 1 THEN '30 min to 1h'\r\n",
                "\t\tWHEN timeSpend = 2 THEN '1h to 2h'\r\n",
                "\t\tWHEN timeSpend = 3 THEN '2h to 3h'\r\n",
                "\t\tWHEN timeSpend = 4 THEN 'More than 3h'\r\n",
                "\t\tEND)\r\n",
                "WHERE timeSpend IN (0,1,2,3,4) \r\n",
                "```\r\n",
                " --Repeating the process for 'location' column.\r\n",
                "```\r\n",
                "ALTER TABLE [dbo].['Starbucks satisfactory survey e$'] \r\n",
                "ALTER COLUMN location varchar(15)\r\n",
                "\r\n",
                "UPDATE [dbo].['Starbucks satisfactory survey e$'] \r\n",
                "SET location =(\r\n",
                "\tCASE\r\n",
                "\t\tWHEN location = 0 THEN 'Within 1km'\r\n",
                "\t\tWHEN location = 1 THEN '1km to 3km'\r\n",
                "\t\tWHEN location = 2 THEN 'More than 3km'\r\n",
                "\t\tEND)\r\n",
                "WHERE location IN (0,1,2)\r\n",
                "```\r\n",
                "--Repeating the process for 'membershipCard' column.\r\n",
                "```\r\n",
                "ALTER TABLE [dbo].['Starbucks satisfactory survey e$'] \r\n",
                "ALTER COLUMN membershipCard varchar(5)\r\n",
                "\r\n",
                "UPDATE [dbo].['Starbucks satisfactory survey e$']\r\n",
                "SET membershipCard = (\r\n",
                "\tCASE\r\n",
                "\t\tWHEN membershipCard = 0 THEN 'Yes'\r\n",
                "\t\tWHEN membershipCard = 1 THEN 'No'\r\n",
                "\t\tEND)\r\n",
                "WHERE membershipCard IN (0,1) \r\n",
                "```\r\n",
                "\r\n",
                "--Checking the dataset.\r\n",
                "```\r\n",
                "SELECT * \r\n",
                "FROM [dbo].['Starbucks satisfactory survey e$'];\r\n",
                "```"
            ],
            "metadata": {
                "azdata_cell_guid": "413f21c9-99c5-4546-a541-b3dcf479303d"
            },
            "attachments": {}
        },
        {
            "cell_type": "markdown",
            "source": [
                "<span style=\"color: rgb(36, 41, 47); font-family: ui-monospace, SFMono-Regular, &quot;SF Mono&quot;, Menlo, Consolas, &quot;Liberation Mono&quot;, monospace; font-size: 12px; white-space: pre;\">--Since the other columns are not relevant for my analysis, I dropped the remaining columns.</span>\n",
                "\n",
                "```\n",
                "ALTER TABLE [dbo].['Starbucks satisfactory survey e$']\n",
                "DROP COLUMN itemPurchaseCoffee ,\n",
                "\t\titempurchaseCold,\n",
                "\t\titemPurchasePastries,\n",
                "\t\titemPurchaseJuices,\n",
                "\t\titemPurchaseSandwiches,\n",
                "\t\titemPurchaseOthers,\n",
                "\t\tspendPurchase,\n",
                "\t\tproductRate,\n",
                "\t\tpriceRate,\n",
                "\t\tpromoRate,\n",
                "\t\tambianceRate,\n",
                "\t\twifiRate,\n",
                "\t\tserviceRate,\n",
                "\t\tchooseRate,\n",
                "\t\tpromoMethodApp,\n",
                "\t\tpromoMethodSoc,\n",
                "\t\tpromoMethodEmail,\n",
                "\t\tpromoMethodDeal,\n",
                "\t\tpromoMethodFriend,\n",
                "\t\tpromoMethodDisplay,\n",
                "\t\tpromoMethodBillboard,\n",
                "\t\tpromoMethodOthers,\n",
                "\t\tloyal;\n",
                "```\n",
                ""
            ],
            "metadata": {
                "azdata_cell_guid": "96847fe3-93da-4b98-94dd-63c6a1041497"
            },
            "attachments": {}
        },
        {
            "cell_type": "markdown",
            "source": [
                "## Final Check"
            ],
            "metadata": {
                "azdata_cell_guid": "4b50bd77-946a-4bb0-baad-8ae16d7828c3"
            },
            "attachments": {}
        },
        {
            "cell_type": "code",
            "source": [
                "SELECT *\r\n",
                "FROM [Project Starbucks].[dbo].['Starbucks satisfactory survey e$']"
            ],
            "metadata": {
                "azdata_cell_guid": "b2bc9061-2d10-4ffa-a121-3f88af3117e3"
            },
            "outputs": [
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "(113 rows affected)"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "display_data",
                    "data": {
                        "text/html": "Total execution time: 00:00:00.053"
                    },
                    "metadata": {}
                },
                {
                    "output_type": "execute_result",
                    "metadata": {},
                    "execution_count": 3,
                    "data": {
                        "application/vnd.dataresource+json": {
                            "schema": {
                                "fields": [
                                    {
                                        "name": "Id"
                                    },
                                    {
                                        "name": "gender"
                                    },
                                    {
                                        "name": "age"
                                    },
                                    {
                                        "name": "status"
                                    },
                                    {
                                        "name": "income"
                                    },
                                    {
                                        "name": "visitNo"
                                    },
                                    {
                                        "name": "method"
                                    },
                                    {
                                        "name": "timeSpend"
                                    },
                                    {
                                        "name": "location"
                                    },
                                    {
                                        "name": "membershipCard"
                                    }
                                ]
                            },
                            "data": [
                                {
                                    "0": "1",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Student",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Dine in",
                                    "7": "30 min to 1h",
                                    "8": "Within 1km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "2",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Student",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Take Away",
                                    "7": "Below 30 minutes",
                                    "8": "1km to 3km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "3",
                                    "1": "Male",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "Less than RM25,000 ",
                                    "5": "Monthly",
                                    "6": "Dine in",
                                    "7": "30 min to 1h",
                                    "8": "More than 3km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "4",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Student",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Take Away",
                                    "7": "Below 30 minutes",
                                    "8": "More than 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "5",
                                    "1": "Male",
                                    "2": "From 20 to 29",
                                    "3": "Student",
                                    "4": "Less than RM25,000 ",
                                    "5": "Monthly",
                                    "6": "Take Away",
                                    "7": "30 min to 1h",
                                    "8": "1km to 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "6",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Student",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Dine in",
                                    "7": "30 min to 1h",
                                    "8": "More than 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "7",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Student",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Dine in",
                                    "7": "Below 30 minutes",
                                    "8": "Within 1km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "8",
                                    "1": "Male",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "RM50,000 – RM100,000",
                                    "5": "Rarely",
                                    "6": "Dine in",
                                    "7": "30 min to 1h",
                                    "8": "More than 3km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "9",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Student",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Drive-thru",
                                    "7": "Below 30 minutes",
                                    "8": "More than 3km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "10",
                                    "1": "Male",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "Less than RM25,000 ",
                                    "5": "Monthly",
                                    "6": "Take Away",
                                    "7": "Below 30 minutes",
                                    "8": "More than 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "11",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Student",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Dine in",
                                    "7": "Below 30 minutes",
                                    "8": "More than 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "12",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Student",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Dine in",
                                    "7": "30 min to 1h",
                                    "8": "More than 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "13",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Student",
                                    "4": "Less than RM25,000 ",
                                    "5": "Weekly",
                                    "6": "Take Away",
                                    "7": "Below 30 minutes",
                                    "8": "1km to 3km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "14",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Student",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Take Away",
                                    "7": "Below 30 minutes",
                                    "8": "1km to 3km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "15",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Student",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Take Away",
                                    "7": "Below 30 minutes",
                                    "8": "Within 1km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "16",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Take Away",
                                    "7": "30 min to 1h",
                                    "8": "More than 3km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "17",
                                    "1": "Male",
                                    "2": "From 30 to 39",
                                    "3": "Employed",
                                    "4": "RM50,000 – RM100,000",
                                    "5": "Monthly",
                                    "6": "Drive-thru",
                                    "7": "Below 30 minutes",
                                    "8": "Within 1km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "18",
                                    "1": "Male",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Dine in",
                                    "7": "Below 30 minutes",
                                    "8": "Within 1km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "19",
                                    "1": "Male",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "RM25,000 – RM50,000",
                                    "5": "Weekly",
                                    "6": "Take Away",
                                    "7": "Below 30 minutes",
                                    "8": "1km to 3km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "20",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Self-Employed",
                                    "4": "RM50,000 – RM100,000",
                                    "5": "Rarely",
                                    "6": "Take Away",
                                    "7": "Below 30 minutes",
                                    "8": "1km to 3km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "21",
                                    "1": "Male",
                                    "2": "From 30 to 39",
                                    "3": "Employed",
                                    "4": "RM100,000 – RM150,000",
                                    "5": "Rarely",
                                    "6": "Take Away",
                                    "7": "Below 30 minutes",
                                    "8": "Within 1km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "22",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Dine in",
                                    "7": "Below 30 minutes",
                                    "8": "Within 1km",
                                    "9": "No"
                                },
                                {
                                    "0": "23",
                                    "1": "Male",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "RM25,000 – RM50,000",
                                    "5": "Rarely",
                                    "6": "Dine in",
                                    "7": "More than 3h",
                                    "8": "Within 1km",
                                    "9": "No"
                                },
                                {
                                    "0": "24",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Student",
                                    "4": "Less than RM25,000 ",
                                    "5": "Monthly",
                                    "6": "Drive-thru",
                                    "7": "1h to 2h",
                                    "8": "1km to 3km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "25",
                                    "1": "Male",
                                    "2": "40 and above",
                                    "3": "Self-Employed",
                                    "4": "RM100,000 – RM150,000",
                                    "5": "Rarely",
                                    "6": "Dine in",
                                    "7": "1h to 2h",
                                    "8": "More than 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "26",
                                    "1": "Male",
                                    "2": "From 30 to 39",
                                    "3": "Employed",
                                    "4": "More than RM150,000",
                                    "5": "Monthly",
                                    "6": "Dine in",
                                    "7": "30 min to 1h",
                                    "8": "1km to 3km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "27",
                                    "1": "Male",
                                    "2": "From 30 to 39",
                                    "3": "Employed",
                                    "4": "More than RM150,000",
                                    "5": "Rarely",
                                    "6": "Drive-thru",
                                    "7": "Below 30 minutes",
                                    "8": "1km to 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "28",
                                    "1": "Male",
                                    "2": "From 20 to 29",
                                    "3": "Self-Employed",
                                    "4": "Less than RM25,000 ",
                                    "5": "Monthly",
                                    "6": "Take Away",
                                    "7": "Below 30 minutes",
                                    "8": "More than 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "29",
                                    "1": "Male",
                                    "2": "40 and above",
                                    "3": "Self-Employed",
                                    "4": "More than RM150,000",
                                    "5": "Weekly",
                                    "6": "Drive-thru",
                                    "7": "Below 30 minutes",
                                    "8": "1km to 3km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "30",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "RM50,000 – RM100,000",
                                    "5": "Rarely",
                                    "6": "Dine in",
                                    "7": "30 min to 1h",
                                    "8": "1km to 3km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "31",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "RM25,000 – RM50,000",
                                    "5": "Monthly",
                                    "6": "Take Away",
                                    "7": "30 min to 1h",
                                    "8": "More than 3km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "32",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "RM50,000 – RM100,000",
                                    "5": "Weekly",
                                    "6": "Drive-thru",
                                    "7": "Below 30 minutes",
                                    "8": "Within 1km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "33",
                                    "1": "Female",
                                    "2": "From 30 to 39",
                                    "3": "Employed",
                                    "4": "RM25,000 – RM50,000",
                                    "5": "Rarely",
                                    "6": "Take Away",
                                    "7": "Below 30 minutes",
                                    "8": "More than 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "34",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "RM25,000 – RM50,000",
                                    "5": "Rarely",
                                    "6": "Dine in",
                                    "7": "30 min to 1h",
                                    "8": "1km to 3km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "35",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "RM25,000 – RM50,000",
                                    "5": "Rarely",
                                    "6": "Take Away",
                                    "7": "Below 30 minutes",
                                    "8": "Within 1km",
                                    "9": "No"
                                },
                                {
                                    "0": "36",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Student",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Take Away",
                                    "7": "Below 30 minutes",
                                    "8": "More than 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "37",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Self-Employed",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Take Away",
                                    "7": "Below 30 minutes",
                                    "8": "Within 1km",
                                    "9": "No"
                                },
                                {
                                    "0": "38",
                                    "1": "Male",
                                    "2": "Below 20",
                                    "3": "Student",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Dine in",
                                    "7": "1h to 2h",
                                    "8": "More than 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "39",
                                    "1": "Male",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Take Away",
                                    "7": "Below 30 minutes",
                                    "8": "More than 3km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "40",
                                    "1": "Male",
                                    "2": "From 30 to 39",
                                    "3": "Employed",
                                    "4": "RM50,000 – RM100,000",
                                    "5": "Rarely",
                                    "6": "Take Away",
                                    "7": "Below 30 minutes",
                                    "8": "Within 1km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "42",
                                    "1": "Male",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "Less than RM25,000 ",
                                    "5": "Monthly",
                                    "6": "Dine in",
                                    "7": "30 min to 1h",
                                    "8": "Within 1km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "43",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "RM25,000 – RM50,000",
                                    "5": "Weekly",
                                    "6": "Dine in",
                                    "7": "30 min to 1h",
                                    "8": "Within 1km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "44",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "Less than RM25,000 ",
                                    "5": "Monthly",
                                    "6": "Take Away",
                                    "7": "Below 30 minutes",
                                    "8": "More than 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "46",
                                    "1": "Female",
                                    "2": "From 30 to 39",
                                    "3": "Student",
                                    "4": "RM50,000 – RM100,000",
                                    "5": "Rarely",
                                    "6": "Take Away",
                                    "7": "Below 30 minutes",
                                    "8": "1km to 3km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "48",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Self-Employed",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Take Away",
                                    "7": "30 min to 1h",
                                    "8": "More than 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "49",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "RM25,000 – RM50,000",
                                    "5": "Rarely",
                                    "6": "Take Away",
                                    "7": "Below 30 minutes",
                                    "8": "Within 1km",
                                    "9": "No"
                                },
                                {
                                    "0": "50",
                                    "1": "Male",
                                    "2": "Below 20",
                                    "3": "Student",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Drive-thru",
                                    "7": "Below 30 minutes",
                                    "8": "Within 1km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "51",
                                    "1": "Male",
                                    "2": "40 and above",
                                    "3": "Employed",
                                    "4": "RM100,000 – RM150,000",
                                    "5": "Rarely",
                                    "6": "Dine in",
                                    "7": "Below 30 minutes",
                                    "8": "More than 3km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "52",
                                    "1": "Female",
                                    "2": "Below 20",
                                    "3": "Student",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Dine in",
                                    "7": "Below 30 minutes",
                                    "8": "More than 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "53",
                                    "1": "Female",
                                    "2": "40 and above",
                                    "3": "Housewife",
                                    "4": "Less than RM25,000 ",
                                    "5": "Monthly",
                                    "6": "Take Away",
                                    "7": "Below 30 minutes",
                                    "8": "More than 3km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "54",
                                    "1": "Female",
                                    "2": "Below 20",
                                    "3": "Student",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Drive-thru",
                                    "7": "Below 30 minutes",
                                    "8": "More than 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "55",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "RM25,000 – RM50,000",
                                    "5": "Rarely",
                                    "6": "Take Away",
                                    "7": "30 min to 1h",
                                    "8": "Within 1km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "56",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "RM25,000 – RM50,000",
                                    "5": "Monthly",
                                    "6": "Take Away",
                                    "7": "30 min to 1h",
                                    "8": "1km to 3km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "57",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Drive-thru",
                                    "7": "Below 30 minutes",
                                    "8": "1km to 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "58",
                                    "1": "Male",
                                    "2": "Below 20",
                                    "3": "Student",
                                    "4": "Less than RM25,000 ",
                                    "5": "Monthly",
                                    "6": "Dine in",
                                    "7": "30 min to 1h",
                                    "8": "More than 3km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "59",
                                    "1": "Male",
                                    "2": "Below 20",
                                    "3": "Student",
                                    "4": "Less than RM25,000 ",
                                    "5": "Monthly",
                                    "6": "Dine in",
                                    "7": "Below 30 minutes",
                                    "8": "1km to 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "60",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Student",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Drive-thru",
                                    "7": "Below 30 minutes",
                                    "8": "More than 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "61",
                                    "1": "Male",
                                    "2": "From 20 to 29",
                                    "3": "Student",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Dine in",
                                    "7": "1h to 2h",
                                    "8": "1km to 3km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "62",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Drive-thru",
                                    "7": "Below 30 minutes",
                                    "8": "1km to 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "63",
                                    "1": "Male",
                                    "2": "From 30 to 39",
                                    "3": "Student",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Dine in",
                                    "7": "30 min to 1h",
                                    "8": "More than 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "64",
                                    "1": "Male",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Take Away",
                                    "7": "30 min to 1h",
                                    "8": "Within 1km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "65",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Take Away",
                                    "7": "Below 30 minutes",
                                    "8": "More than 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "66",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Student",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Dine in",
                                    "7": "30 min to 1h",
                                    "8": "1km to 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "67",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Self-Employed",
                                    "4": "RM25,000 – RM50,000",
                                    "5": "Monthly",
                                    "6": "Dine in",
                                    "7": "Below 30 minutes",
                                    "8": "Within 1km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "69",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Dine in",
                                    "7": "Below 30 minutes",
                                    "8": "More than 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "70",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "RM25,000 – RM50,000",
                                    "5": "Rarely",
                                    "6": "Dine in",
                                    "7": "30 min to 1h",
                                    "8": "1km to 3km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "71",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Take Away",
                                    "7": "Below 30 minutes",
                                    "8": "Within 1km",
                                    "9": "No"
                                },
                                {
                                    "0": "72",
                                    "1": "Male",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "RM25,000 – RM50,000",
                                    "5": "Weekly",
                                    "6": "Take Away",
                                    "7": "1h to 2h",
                                    "8": "Within 1km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "73",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "Less than RM25,000 ",
                                    "5": "Monthly",
                                    "6": "Take Away",
                                    "7": "Below 30 minutes",
                                    "8": "More than 3km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "74",
                                    "1": "Male",
                                    "2": "From 30 to 39",
                                    "3": "Employed",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Take Away",
                                    "7": "Below 30 minutes",
                                    "8": "1km to 3km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "75",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Housewife",
                                    "4": "RM50,000 – RM100,000",
                                    "5": "Rarely",
                                    "6": "Drive-thru",
                                    "7": "Below 30 minutes",
                                    "8": "More than 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "76",
                                    "1": "Male",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "RM25,000 – RM50,000",
                                    "5": "Rarely",
                                    "6": "Take Away",
                                    "7": "Below 30 minutes",
                                    "8": "More than 3km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "77",
                                    "1": "Male",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Take Away",
                                    "7": "Below 30 minutes",
                                    "8": "1km to 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "78",
                                    "1": "Male",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "RM50,000 – RM100,000",
                                    "5": "Monthly",
                                    "6": "Dine in",
                                    "7": "30 min to 1h",
                                    "8": "More than 3km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "79",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Student",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Take Away",
                                    "7": "Below 30 minutes",
                                    "8": "More than 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "80",
                                    "1": "Female",
                                    "2": "Below 20",
                                    "3": "Student",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Take Away",
                                    "7": "Below 30 minutes",
                                    "8": "More than 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "81",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "RM50,000 – RM100,000",
                                    "5": "Monthly",
                                    "6": "Drive-thru",
                                    "7": "More than 3h",
                                    "8": "1km to 3km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "83",
                                    "1": "Male",
                                    "2": "From 20 to 29",
                                    "3": "Self-Employed",
                                    "4": "RM50,000 – RM100,000",
                                    "5": "Rarely",
                                    "6": "Dine in",
                                    "7": "1h to 2h",
                                    "8": "More than 3km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "84",
                                    "1": "Male",
                                    "2": "From 30 to 39",
                                    "3": "Self-Employed",
                                    "4": "RM50,000 – RM100,000",
                                    "5": "Weekly",
                                    "6": "Take Away",
                                    "7": "30 min to 1h",
                                    "8": "1km to 3km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "85",
                                    "1": "Male",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "RM25,000 – RM50,000",
                                    "5": "Rarely",
                                    "6": "Dine in",
                                    "7": "1h to 2h",
                                    "8": "More than 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "86",
                                    "1": "Male",
                                    "2": "From 30 to 39",
                                    "3": "Self-Employed",
                                    "4": "More than RM150,000",
                                    "5": "Monthly",
                                    "6": "Dine in",
                                    "7": "2h to 3h",
                                    "8": "More than 3km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "87",
                                    "1": "Male",
                                    "2": "From 20 to 29",
                                    "3": "Self-Employed",
                                    "4": "More than RM150,000",
                                    "5": "Rarely",
                                    "6": "Drive-thru",
                                    "7": "30 min to 1h",
                                    "8": "More than 3km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "88",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Dine in",
                                    "7": "Below 30 minutes",
                                    "8": "1km to 3km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "89",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "RM25,000 – RM50,000",
                                    "5": "Rarely",
                                    "6": "Take Away",
                                    "7": "Below 30 minutes",
                                    "8": "Within 1km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "90",
                                    "1": "Male",
                                    "2": "From 20 to 29",
                                    "3": "Self-Employed",
                                    "4": "RM25,000 – RM50,000",
                                    "5": "Rarely",
                                    "6": "Dine in",
                                    "7": "Below 30 minutes",
                                    "8": "1km to 3km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "91",
                                    "1": "Female",
                                    "2": "From 30 to 39",
                                    "3": "Employed",
                                    "4": "RM50,000 – RM100,000",
                                    "5": "Weekly",
                                    "6": "Dine in",
                                    "7": "1h to 2h",
                                    "8": "More than 3km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "92",
                                    "1": "Female",
                                    "2": "From 30 to 39",
                                    "3": "Employed",
                                    "4": "RM25,000 – RM50,000",
                                    "5": "Monthly",
                                    "6": "Take Away",
                                    "7": "30 min to 1h",
                                    "8": "Within 1km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "94",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Take Away",
                                    "7": "Below 30 minutes",
                                    "8": "More than 3km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "95",
                                    "1": "Male",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "RM50,000 – RM100,000",
                                    "5": "Monthly",
                                    "6": "Take Away",
                                    "7": "Below 30 minutes",
                                    "8": "More than 3km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "96",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "RM25,000 – RM50,000",
                                    "5": "Rarely",
                                    "6": "Dine in",
                                    "7": "30 min to 1h",
                                    "8": "1km to 3km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "97",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Self-Employed",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Take Away",
                                    "7": "Below 30 minutes",
                                    "8": "More than 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "98",
                                    "1": "Female",
                                    "2": "From 30 to 39",
                                    "3": "Employed",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Others",
                                    "7": "Below 30 minutes",
                                    "8": "Within 1km",
                                    "9": "No"
                                },
                                {
                                    "0": "99",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "RM25,000 – RM50,000",
                                    "5": "Rarely",
                                    "6": "Drive-thru",
                                    "7": "Below 30 minutes",
                                    "8": "1km to 3km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "100",
                                    "1": "Male",
                                    "2": "From 30 to 39",
                                    "3": "Employed",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Drive-thru",
                                    "7": "30 min to 1h",
                                    "8": "More than 3km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "101",
                                    "1": "Male",
                                    "2": "From 20 to 29",
                                    "3": "Student",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Drive-thru",
                                    "7": "30 min to 1h",
                                    "8": "More than 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "102",
                                    "1": "Male",
                                    "2": "From 20 to 29",
                                    "3": "Student",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Dine in",
                                    "7": "30 min to 1h",
                                    "8": "More than 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "103",
                                    "1": "Male",
                                    "2": "From 20 to 29",
                                    "3": "Self-Employed",
                                    "4": "RM50,000 – RM100,000",
                                    "5": "Daily",
                                    "6": "Drive-thru",
                                    "7": "Below 30 minutes",
                                    "8": "More than 3km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "104",
                                    "1": "Male",
                                    "2": "From 30 to 39",
                                    "3": "Employed",
                                    "4": "RM25,000 – RM50,000",
                                    "5": "Weekly",
                                    "6": "Dine in",
                                    "7": "1h to 2h",
                                    "8": "More than 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "105",
                                    "1": "Male",
                                    "2": "Below 20",
                                    "3": "Student",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Drive-thru",
                                    "7": "30 min to 1h",
                                    "8": "More than 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "106",
                                    "1": "Male",
                                    "2": "40 and above",
                                    "3": "Employed",
                                    "4": "RM50,000 – RM100,000",
                                    "5": "Monthly",
                                    "6": "Drive-thru",
                                    "7": "30 min to 1h",
                                    "8": "More than 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "107",
                                    "1": "Male",
                                    "2": "From 20 to 29",
                                    "3": "Student",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Take Away",
                                    "7": "Below 30 minutes",
                                    "8": "More than 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "110",
                                    "1": "Male",
                                    "2": "From 20 to 29",
                                    "3": "Student",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Dine in",
                                    "7": "Below 30 minutes",
                                    "8": "More than 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "111",
                                    "1": "Male",
                                    "2": "From 20 to 29",
                                    "3": "Student",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Take Away",
                                    "7": "Below 30 minutes",
                                    "8": "More than 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "112",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "Less than RM25,000 ",
                                    "5": "Monthly",
                                    "6": "Take Away",
                                    "7": "Below 30 minutes",
                                    "8": "More than 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "114",
                                    "1": "Female",
                                    "2": "Below 20",
                                    "3": "Student",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Take Away",
                                    "7": "Below 30 minutes",
                                    "8": "More than 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "115",
                                    "1": "Male",
                                    "2": "40 and above",
                                    "3": "Self-Employed",
                                    "4": "RM25,000 – RM50,000",
                                    "5": "Rarely",
                                    "6": "Dine in",
                                    "7": "30 min to 1h",
                                    "8": "More than 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "116",
                                    "1": "Male",
                                    "2": "Below 20",
                                    "3": "Student",
                                    "4": "Less than RM25,000 ",
                                    "5": "Daily",
                                    "6": "Take Away",
                                    "7": "Below 30 minutes",
                                    "8": "More than 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "117",
                                    "1": "Male",
                                    "2": "From 30 to 39",
                                    "3": "Student",
                                    "4": "Less than RM25,000 ",
                                    "5": "Monthly",
                                    "6": "Dine in",
                                    "7": "1h to 2h",
                                    "8": "More than 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "118",
                                    "1": "Male",
                                    "2": "40 and above",
                                    "3": "Self-Employed",
                                    "4": "RM25,000 – RM50,000",
                                    "5": "Monthly",
                                    "6": "Dine in",
                                    "7": "1h to 2h",
                                    "8": "1km to 3km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "119",
                                    "1": "Male",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "Less than RM25,000 ",
                                    "5": "Monthly",
                                    "6": "Dine in",
                                    "7": "1h to 2h",
                                    "8": "1km to 3km",
                                    "9": "Yes"
                                },
                                {
                                    "0": "120",
                                    "1": "Male",
                                    "2": "From 20 to 29",
                                    "3": "Student",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Dine in",
                                    "7": "30 min to 1h",
                                    "8": "1km to 3km",
                                    "9": "No"
                                },
                                {
                                    "0": "121",
                                    "1": "Female",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "Less than RM25,000 ",
                                    "5": "Rarely",
                                    "6": "Take Away",
                                    "7": "Below 30 minutes",
                                    "8": "Within 1km",
                                    "9": "No"
                                },
                                {
                                    "0": "122",
                                    "1": "Male",
                                    "2": "From 20 to 29",
                                    "3": "Employed",
                                    "4": "RM50,000 – RM100,000",
                                    "5": "Rarely",
                                    "6": "Dine in",
                                    "7": "30 min to 1h",
                                    "8": "1km to 3km",
                                    "9": "No"
                                }
                            ]
                        },
                        "text/html": [
                            "<table>",
                            "<tr><th>Id</th><th>gender</th><th>age</th><th>status</th><th>income</th><th>visitNo</th><th>method</th><th>timeSpend</th><th>location</th><th>membershipCard</th></tr>",
                            "<tr><td>1</td><td>Female</td><td>From 20 to 29</td><td>Student</td><td>Less than RM25,000 </td><td>Rarely</td><td>Dine in</td><td>30 min to 1h</td><td>Within 1km</td><td>Yes</td></tr>",
                            "<tr><td>2</td><td>Female</td><td>From 20 to 29</td><td>Student</td><td>Less than RM25,000 </td><td>Rarely</td><td>Take Away</td><td>Below 30 minutes</td><td>1km to 3km</td><td>Yes</td></tr>",
                            "<tr><td>3</td><td>Male</td><td>From 20 to 29</td><td>Employed</td><td>Less than RM25,000 </td><td>Monthly</td><td>Dine in</td><td>30 min to 1h</td><td>More than 3km</td><td>Yes</td></tr>",
                            "<tr><td>4</td><td>Female</td><td>From 20 to 29</td><td>Student</td><td>Less than RM25,000 </td><td>Rarely</td><td>Take Away</td><td>Below 30 minutes</td><td>More than 3km</td><td>No</td></tr>",
                            "<tr><td>5</td><td>Male</td><td>From 20 to 29</td><td>Student</td><td>Less than RM25,000 </td><td>Monthly</td><td>Take Away</td><td>30 min to 1h</td><td>1km to 3km</td><td>No</td></tr>",
                            "<tr><td>6</td><td>Female</td><td>From 20 to 29</td><td>Student</td><td>Less than RM25,000 </td><td>Rarely</td><td>Dine in</td><td>30 min to 1h</td><td>More than 3km</td><td>No</td></tr>",
                            "<tr><td>7</td><td>Female</td><td>From 20 to 29</td><td>Student</td><td>Less than RM25,000 </td><td>Rarely</td><td>Dine in</td><td>Below 30 minutes</td><td>Within 1km</td><td>Yes</td></tr>",
                            "<tr><td>8</td><td>Male</td><td>From 20 to 29</td><td>Employed</td><td>RM50,000 – RM100,000</td><td>Rarely</td><td>Dine in</td><td>30 min to 1h</td><td>More than 3km</td><td>Yes</td></tr>",
                            "<tr><td>9</td><td>Female</td><td>From 20 to 29</td><td>Student</td><td>Less than RM25,000 </td><td>Rarely</td><td>Drive-thru</td><td>Below 30 minutes</td><td>More than 3km</td><td>Yes</td></tr>",
                            "<tr><td>10</td><td>Male</td><td>From 20 to 29</td><td>Employed</td><td>Less than RM25,000 </td><td>Monthly</td><td>Take Away</td><td>Below 30 minutes</td><td>More than 3km</td><td>No</td></tr>",
                            "<tr><td>11</td><td>Female</td><td>From 20 to 29</td><td>Student</td><td>Less than RM25,000 </td><td>Rarely</td><td>Dine in</td><td>Below 30 minutes</td><td>More than 3km</td><td>No</td></tr>",
                            "<tr><td>12</td><td>Female</td><td>From 20 to 29</td><td>Student</td><td>Less than RM25,000 </td><td>Rarely</td><td>Dine in</td><td>30 min to 1h</td><td>More than 3km</td><td>No</td></tr>",
                            "<tr><td>13</td><td>Female</td><td>From 20 to 29</td><td>Student</td><td>Less than RM25,000 </td><td>Weekly</td><td>Take Away</td><td>Below 30 minutes</td><td>1km to 3km</td><td>Yes</td></tr>",
                            "<tr><td>14</td><td>Female</td><td>From 20 to 29</td><td>Student</td><td>Less than RM25,000 </td><td>Rarely</td><td>Take Away</td><td>Below 30 minutes</td><td>1km to 3km</td><td>Yes</td></tr>",
                            "<tr><td>15</td><td>Female</td><td>From 20 to 29</td><td>Student</td><td>Less than RM25,000 </td><td>Rarely</td><td>Take Away</td><td>Below 30 minutes</td><td>Within 1km</td><td>Yes</td></tr>",
                            "<tr><td>16</td><td>Female</td><td>From 20 to 29</td><td>Employed</td><td>Less than RM25,000 </td><td>Rarely</td><td>Take Away</td><td>30 min to 1h</td><td>More than 3km</td><td>Yes</td></tr>",
                            "<tr><td>17</td><td>Male</td><td>From 30 to 39</td><td>Employed</td><td>RM50,000 – RM100,000</td><td>Monthly</td><td>Drive-thru</td><td>Below 30 minutes</td><td>Within 1km</td><td>Yes</td></tr>",
                            "<tr><td>18</td><td>Male</td><td>From 20 to 29</td><td>Employed</td><td>Less than RM25,000 </td><td>Rarely</td><td>Dine in</td><td>Below 30 minutes</td><td>Within 1km</td><td>Yes</td></tr>",
                            "<tr><td>19</td><td>Male</td><td>From 20 to 29</td><td>Employed</td><td>RM25,000 – RM50,000</td><td>Weekly</td><td>Take Away</td><td>Below 30 minutes</td><td>1km to 3km</td><td>Yes</td></tr>",
                            "<tr><td>20</td><td>Female</td><td>From 20 to 29</td><td>Self-Employed</td><td>RM50,000 – RM100,000</td><td>Rarely</td><td>Take Away</td><td>Below 30 minutes</td><td>1km to 3km</td><td>Yes</td></tr>",
                            "<tr><td>21</td><td>Male</td><td>From 30 to 39</td><td>Employed</td><td>RM100,000 – RM150,000</td><td>Rarely</td><td>Take Away</td><td>Below 30 minutes</td><td>Within 1km</td><td>Yes</td></tr>",
                            "<tr><td>22</td><td>Female</td><td>From 20 to 29</td><td>Employed</td><td>Less than RM25,000 </td><td>Rarely</td><td>Dine in</td><td>Below 30 minutes</td><td>Within 1km</td><td>No</td></tr>",
                            "<tr><td>23</td><td>Male</td><td>From 20 to 29</td><td>Employed</td><td>RM25,000 – RM50,000</td><td>Rarely</td><td>Dine in</td><td>More than 3h</td><td>Within 1km</td><td>No</td></tr>",
                            "<tr><td>24</td><td>Female</td><td>From 20 to 29</td><td>Student</td><td>Less than RM25,000 </td><td>Monthly</td><td>Drive-thru</td><td>1h to 2h</td><td>1km to 3km</td><td>Yes</td></tr>",
                            "<tr><td>25</td><td>Male</td><td>40 and above</td><td>Self-Employed</td><td>RM100,000 – RM150,000</td><td>Rarely</td><td>Dine in</td><td>1h to 2h</td><td>More than 3km</td><td>No</td></tr>",
                            "<tr><td>26</td><td>Male</td><td>From 30 to 39</td><td>Employed</td><td>More than RM150,000</td><td>Monthly</td><td>Dine in</td><td>30 min to 1h</td><td>1km to 3km</td><td>Yes</td></tr>",
                            "<tr><td>27</td><td>Male</td><td>From 30 to 39</td><td>Employed</td><td>More than RM150,000</td><td>Rarely</td><td>Drive-thru</td><td>Below 30 minutes</td><td>1km to 3km</td><td>No</td></tr>",
                            "<tr><td>28</td><td>Male</td><td>From 20 to 29</td><td>Self-Employed</td><td>Less than RM25,000 </td><td>Monthly</td><td>Take Away</td><td>Below 30 minutes</td><td>More than 3km</td><td>No</td></tr>",
                            "<tr><td>29</td><td>Male</td><td>40 and above</td><td>Self-Employed</td><td>More than RM150,000</td><td>Weekly</td><td>Drive-thru</td><td>Below 30 minutes</td><td>1km to 3km</td><td>Yes</td></tr>",
                            "<tr><td>30</td><td>Female</td><td>From 20 to 29</td><td>Employed</td><td>RM50,000 – RM100,000</td><td>Rarely</td><td>Dine in</td><td>30 min to 1h</td><td>1km to 3km</td><td>Yes</td></tr>",
                            "<tr><td>31</td><td>Female</td><td>From 20 to 29</td><td>Employed</td><td>RM25,000 – RM50,000</td><td>Monthly</td><td>Take Away</td><td>30 min to 1h</td><td>More than 3km</td><td>Yes</td></tr>",
                            "<tr><td>32</td><td>Female</td><td>From 20 to 29</td><td>Employed</td><td>RM50,000 – RM100,000</td><td>Weekly</td><td>Drive-thru</td><td>Below 30 minutes</td><td>Within 1km</td><td>Yes</td></tr>",
                            "<tr><td>33</td><td>Female</td><td>From 30 to 39</td><td>Employed</td><td>RM25,000 – RM50,000</td><td>Rarely</td><td>Take Away</td><td>Below 30 minutes</td><td>More than 3km</td><td>No</td></tr>",
                            "<tr><td>34</td><td>Female</td><td>From 20 to 29</td><td>Employed</td><td>RM25,000 – RM50,000</td><td>Rarely</td><td>Dine in</td><td>30 min to 1h</td><td>1km to 3km</td><td>Yes</td></tr>",
                            "<tr><td>35</td><td>Female</td><td>From 20 to 29</td><td>Employed</td><td>RM25,000 – RM50,000</td><td>Rarely</td><td>Take Away</td><td>Below 30 minutes</td><td>Within 1km</td><td>No</td></tr>",
                            "<tr><td>36</td><td>Female</td><td>From 20 to 29</td><td>Student</td><td>Less than RM25,000 </td><td>Rarely</td><td>Take Away</td><td>Below 30 minutes</td><td>More than 3km</td><td>No</td></tr>",
                            "<tr><td>37</td><td>Female</td><td>From 20 to 29</td><td>Self-Employed</td><td>Less than RM25,000 </td><td>Rarely</td><td>Take Away</td><td>Below 30 minutes</td><td>Within 1km</td><td>No</td></tr>",
                            "<tr><td>38</td><td>Male</td><td>Below 20</td><td>Student</td><td>Less than RM25,000 </td><td>Rarely</td><td>Dine in</td><td>1h to 2h</td><td>More than 3km</td><td>No</td></tr>",
                            "<tr><td>39</td><td>Male</td><td>From 20 to 29</td><td>Employed</td><td>Less than RM25,000 </td><td>Rarely</td><td>Take Away</td><td>Below 30 minutes</td><td>More than 3km</td><td>Yes</td></tr>",
                            "<tr><td>40</td><td>Male</td><td>From 30 to 39</td><td>Employed</td><td>RM50,000 – RM100,000</td><td>Rarely</td><td>Take Away</td><td>Below 30 minutes</td><td>Within 1km</td><td>Yes</td></tr>",
                            "<tr><td>42</td><td>Male</td><td>From 20 to 29</td><td>Employed</td><td>Less than RM25,000 </td><td>Monthly</td><td>Dine in</td><td>30 min to 1h</td><td>Within 1km</td><td>Yes</td></tr>",
                            "<tr><td>43</td><td>Female</td><td>From 20 to 29</td><td>Employed</td><td>RM25,000 – RM50,000</td><td>Weekly</td><td>Dine in</td><td>30 min to 1h</td><td>Within 1km</td><td>Yes</td></tr>",
                            "<tr><td>44</td><td>Female</td><td>From 20 to 29</td><td>Employed</td><td>Less than RM25,000 </td><td>Monthly</td><td>Take Away</td><td>Below 30 minutes</td><td>More than 3km</td><td>No</td></tr>",
                            "<tr><td>46</td><td>Female</td><td>From 30 to 39</td><td>Student</td><td>RM50,000 – RM100,000</td><td>Rarely</td><td>Take Away</td><td>Below 30 minutes</td><td>1km to 3km</td><td>Yes</td></tr>",
                            "<tr><td>48</td><td>Female</td><td>From 20 to 29</td><td>Self-Employed</td><td>Less than RM25,000 </td><td>Rarely</td><td>Take Away</td><td>30 min to 1h</td><td>More than 3km</td><td>No</td></tr>",
                            "<tr><td>49</td><td>Female</td><td>From 20 to 29</td><td>Employed</td><td>RM25,000 – RM50,000</td><td>Rarely</td><td>Take Away</td><td>Below 30 minutes</td><td>Within 1km</td><td>No</td></tr>",
                            "<tr><td>50</td><td>Male</td><td>Below 20</td><td>Student</td><td>Less than RM25,000 </td><td>Rarely</td><td>Drive-thru</td><td>Below 30 minutes</td><td>Within 1km</td><td>Yes</td></tr>",
                            "<tr><td>51</td><td>Male</td><td>40 and above</td><td>Employed</td><td>RM100,000 – RM150,000</td><td>Rarely</td><td>Dine in</td><td>Below 30 minutes</td><td>More than 3km</td><td>Yes</td></tr>",
                            "<tr><td>52</td><td>Female</td><td>Below 20</td><td>Student</td><td>Less than RM25,000 </td><td>Rarely</td><td>Dine in</td><td>Below 30 minutes</td><td>More than 3km</td><td>No</td></tr>",
                            "<tr><td>53</td><td>Female</td><td>40 and above</td><td>Housewife</td><td>Less than RM25,000 </td><td>Monthly</td><td>Take Away</td><td>Below 30 minutes</td><td>More than 3km</td><td>Yes</td></tr>",
                            "<tr><td>54</td><td>Female</td><td>Below 20</td><td>Student</td><td>Less than RM25,000 </td><td>Rarely</td><td>Drive-thru</td><td>Below 30 minutes</td><td>More than 3km</td><td>No</td></tr>",
                            "<tr><td>55</td><td>Female</td><td>From 20 to 29</td><td>Employed</td><td>RM25,000 – RM50,000</td><td>Rarely</td><td>Take Away</td><td>30 min to 1h</td><td>Within 1km</td><td>Yes</td></tr>",
                            "<tr><td>56</td><td>Female</td><td>From 20 to 29</td><td>Employed</td><td>RM25,000 – RM50,000</td><td>Monthly</td><td>Take Away</td><td>30 min to 1h</td><td>1km to 3km</td><td>Yes</td></tr>",
                            "<tr><td>57</td><td>Female</td><td>From 20 to 29</td><td>Employed</td><td>Less than RM25,000 </td><td>Rarely</td><td>Drive-thru</td><td>Below 30 minutes</td><td>1km to 3km</td><td>No</td></tr>",
                            "<tr><td>58</td><td>Male</td><td>Below 20</td><td>Student</td><td>Less than RM25,000 </td><td>Monthly</td><td>Dine in</td><td>30 min to 1h</td><td>More than 3km</td><td>Yes</td></tr>",
                            "<tr><td>59</td><td>Male</td><td>Below 20</td><td>Student</td><td>Less than RM25,000 </td><td>Monthly</td><td>Dine in</td><td>Below 30 minutes</td><td>1km to 3km</td><td>No</td></tr>",
                            "<tr><td>60</td><td>Female</td><td>From 20 to 29</td><td>Student</td><td>Less than RM25,000 </td><td>Rarely</td><td>Drive-thru</td><td>Below 30 minutes</td><td>More than 3km</td><td>No</td></tr>",
                            "<tr><td>61</td><td>Male</td><td>From 20 to 29</td><td>Student</td><td>Less than RM25,000 </td><td>Rarely</td><td>Dine in</td><td>1h to 2h</td><td>1km to 3km</td><td>Yes</td></tr>",
                            "<tr><td>62</td><td>Female</td><td>From 20 to 29</td><td>Employed</td><td>Less than RM25,000 </td><td>Rarely</td><td>Drive-thru</td><td>Below 30 minutes</td><td>1km to 3km</td><td>No</td></tr>",
                            "<tr><td>63</td><td>Male</td><td>From 30 to 39</td><td>Student</td><td>Less than RM25,000 </td><td>Rarely</td><td>Dine in</td><td>30 min to 1h</td><td>More than 3km</td><td>No</td></tr>",
                            "<tr><td>64</td><td>Male</td><td>From 20 to 29</td><td>Employed</td><td>Less than RM25,000 </td><td>Rarely</td><td>Take Away</td><td>30 min to 1h</td><td>Within 1km</td><td>Yes</td></tr>",
                            "<tr><td>65</td><td>Female</td><td>From 20 to 29</td><td>Employed</td><td>Less than RM25,000 </td><td>Rarely</td><td>Take Away</td><td>Below 30 minutes</td><td>More than 3km</td><td>No</td></tr>",
                            "<tr><td>66</td><td>Female</td><td>From 20 to 29</td><td>Student</td><td>Less than RM25,000 </td><td>Rarely</td><td>Dine in</td><td>30 min to 1h</td><td>1km to 3km</td><td>No</td></tr>",
                            "<tr><td>67</td><td>Female</td><td>From 20 to 29</td><td>Self-Employed</td><td>RM25,000 – RM50,000</td><td>Monthly</td><td>Dine in</td><td>Below 30 minutes</td><td>Within 1km</td><td>Yes</td></tr>",
                            "<tr><td>69</td><td>Female</td><td>From 20 to 29</td><td>Employed</td><td>Less than RM25,000 </td><td>Rarely</td><td>Dine in</td><td>Below 30 minutes</td><td>More than 3km</td><td>No</td></tr>",
                            "<tr><td>70</td><td>Female</td><td>From 20 to 29</td><td>Employed</td><td>RM25,000 – RM50,000</td><td>Rarely</td><td>Dine in</td><td>30 min to 1h</td><td>1km to 3km</td><td>Yes</td></tr>",
                            "<tr><td>71</td><td>Female</td><td>From 20 to 29</td><td>Employed</td><td>Less than RM25,000 </td><td>Rarely</td><td>Take Away</td><td>Below 30 minutes</td><td>Within 1km</td><td>No</td></tr>",
                            "<tr><td>72</td><td>Male</td><td>From 20 to 29</td><td>Employed</td><td>RM25,000 – RM50,000</td><td>Weekly</td><td>Take Away</td><td>1h to 2h</td><td>Within 1km</td><td>Yes</td></tr>",
                            "<tr><td>73</td><td>Female</td><td>From 20 to 29</td><td>Employed</td><td>Less than RM25,000 </td><td>Monthly</td><td>Take Away</td><td>Below 30 minutes</td><td>More than 3km</td><td>Yes</td></tr>",
                            "<tr><td>74</td><td>Male</td><td>From 30 to 39</td><td>Employed</td><td>Less than RM25,000 </td><td>Rarely</td><td>Take Away</td><td>Below 30 minutes</td><td>1km to 3km</td><td>Yes</td></tr>",
                            "<tr><td>75</td><td>Female</td><td>From 20 to 29</td><td>Housewife</td><td>RM50,000 – RM100,000</td><td>Rarely</td><td>Drive-thru</td><td>Below 30 minutes</td><td>More than 3km</td><td>No</td></tr>",
                            "<tr><td>76</td><td>Male</td><td>From 20 to 29</td><td>Employed</td><td>RM25,000 – RM50,000</td><td>Rarely</td><td>Take Away</td><td>Below 30 minutes</td><td>More than 3km</td><td>Yes</td></tr>",
                            "<tr><td>77</td><td>Male</td><td>From 20 to 29</td><td>Employed</td><td>Less than RM25,000 </td><td>Rarely</td><td>Take Away</td><td>Below 30 minutes</td><td>1km to 3km</td><td>No</td></tr>",
                            "<tr><td>78</td><td>Male</td><td>From 20 to 29</td><td>Employed</td><td>RM50,000 – RM100,000</td><td>Monthly</td><td>Dine in</td><td>30 min to 1h</td><td>More than 3km</td><td>Yes</td></tr>",
                            "<tr><td>79</td><td>Female</td><td>From 20 to 29</td><td>Student</td><td>Less than RM25,000 </td><td>Rarely</td><td>Take Away</td><td>Below 30 minutes</td><td>More than 3km</td><td>No</td></tr>",
                            "<tr><td>80</td><td>Female</td><td>Below 20</td><td>Student</td><td>Less than RM25,000 </td><td>Rarely</td><td>Take Away</td><td>Below 30 minutes</td><td>More than 3km</td><td>No</td></tr>",
                            "<tr><td>81</td><td>Female</td><td>From 20 to 29</td><td>Employed</td><td>RM50,000 – RM100,000</td><td>Monthly</td><td>Drive-thru</td><td>More than 3h</td><td>1km to 3km</td><td>Yes</td></tr>",
                            "<tr><td>83</td><td>Male</td><td>From 20 to 29</td><td>Self-Employed</td><td>RM50,000 – RM100,000</td><td>Rarely</td><td>Dine in</td><td>1h to 2h</td><td>More than 3km</td><td>Yes</td></tr>",
                            "<tr><td>84</td><td>Male</td><td>From 30 to 39</td><td>Self-Employed</td><td>RM50,000 – RM100,000</td><td>Weekly</td><td>Take Away</td><td>30 min to 1h</td><td>1km to 3km</td><td>Yes</td></tr>",
                            "<tr><td>85</td><td>Male</td><td>From 20 to 29</td><td>Employed</td><td>RM25,000 – RM50,000</td><td>Rarely</td><td>Dine in</td><td>1h to 2h</td><td>More than 3km</td><td>No</td></tr>",
                            "<tr><td>86</td><td>Male</td><td>From 30 to 39</td><td>Self-Employed</td><td>More than RM150,000</td><td>Monthly</td><td>Dine in</td><td>2h to 3h</td><td>More than 3km</td><td>Yes</td></tr>",
                            "<tr><td>87</td><td>Male</td><td>From 20 to 29</td><td>Self-Employed</td><td>More than RM150,000</td><td>Rarely</td><td>Drive-thru</td><td>30 min to 1h</td><td>More than 3km</td><td>Yes</td></tr>",
                            "<tr><td>88</td><td>Female</td><td>From 20 to 29</td><td>Employed</td><td>Less than RM25,000 </td><td>Rarely</td><td>Dine in</td><td>Below 30 minutes</td><td>1km to 3km</td><td>Yes</td></tr>",
                            "<tr><td>89</td><td>Female</td><td>From 20 to 29</td><td>Employed</td><td>RM25,000 – RM50,000</td><td>Rarely</td><td>Take Away</td><td>Below 30 minutes</td><td>Within 1km</td><td>Yes</td></tr>",
                            "<tr><td>90</td><td>Male</td><td>From 20 to 29</td><td>Self-Employed</td><td>RM25,000 – RM50,000</td><td>Rarely</td><td>Dine in</td><td>Below 30 minutes</td><td>1km to 3km</td><td>Yes</td></tr>",
                            "<tr><td>91</td><td>Female</td><td>From 30 to 39</td><td>Employed</td><td>RM50,000 – RM100,000</td><td>Weekly</td><td>Dine in</td><td>1h to 2h</td><td>More than 3km</td><td>Yes</td></tr>",
                            "<tr><td>92</td><td>Female</td><td>From 30 to 39</td><td>Employed</td><td>RM25,000 – RM50,000</td><td>Monthly</td><td>Take Away</td><td>30 min to 1h</td><td>Within 1km</td><td>Yes</td></tr>",
                            "<tr><td>94</td><td>Female</td><td>From 20 to 29</td><td>Employed</td><td>Less than RM25,000 </td><td>Rarely</td><td>Take Away</td><td>Below 30 minutes</td><td>More than 3km</td><td>Yes</td></tr>",
                            "<tr><td>95</td><td>Male</td><td>From 20 to 29</td><td>Employed</td><td>RM50,000 – RM100,000</td><td>Monthly</td><td>Take Away</td><td>Below 30 minutes</td><td>More than 3km</td><td>Yes</td></tr>",
                            "<tr><td>96</td><td>Female</td><td>From 20 to 29</td><td>Employed</td><td>RM25,000 – RM50,000</td><td>Rarely</td><td>Dine in</td><td>30 min to 1h</td><td>1km to 3km</td><td>Yes</td></tr>",
                            "<tr><td>97</td><td>Female</td><td>From 20 to 29</td><td>Self-Employed</td><td>Less than RM25,000 </td><td>Rarely</td><td>Take Away</td><td>Below 30 minutes</td><td>More than 3km</td><td>No</td></tr>",
                            "<tr><td>98</td><td>Female</td><td>From 30 to 39</td><td>Employed</td><td>Less than RM25,000 </td><td>Rarely</td><td>Others</td><td>Below 30 minutes</td><td>Within 1km</td><td>No</td></tr>",
                            "<tr><td>99</td><td>Female</td><td>From 20 to 29</td><td>Employed</td><td>RM25,000 – RM50,000</td><td>Rarely</td><td>Drive-thru</td><td>Below 30 minutes</td><td>1km to 3km</td><td>Yes</td></tr>",
                            "<tr><td>100</td><td>Male</td><td>From 30 to 39</td><td>Employed</td><td>Less than RM25,000 </td><td>Rarely</td><td>Drive-thru</td><td>30 min to 1h</td><td>More than 3km</td><td>Yes</td></tr>",
                            "<tr><td>101</td><td>Male</td><td>From 20 to 29</td><td>Student</td><td>Less than RM25,000 </td><td>Rarely</td><td>Drive-thru</td><td>30 min to 1h</td><td>More than 3km</td><td>No</td></tr>",
                            "<tr><td>102</td><td>Male</td><td>From 20 to 29</td><td>Student</td><td>Less than RM25,000 </td><td>Rarely</td><td>Dine in</td><td>30 min to 1h</td><td>More than 3km</td><td>No</td></tr>",
                            "<tr><td>103</td><td>Male</td><td>From 20 to 29</td><td>Self-Employed</td><td>RM50,000 – RM100,000</td><td>Daily</td><td>Drive-thru</td><td>Below 30 minutes</td><td>More than 3km</td><td>Yes</td></tr>",
                            "<tr><td>104</td><td>Male</td><td>From 30 to 39</td><td>Employed</td><td>RM25,000 – RM50,000</td><td>Weekly</td><td>Dine in</td><td>1h to 2h</td><td>More than 3km</td><td>No</td></tr>",
                            "<tr><td>105</td><td>Male</td><td>Below 20</td><td>Student</td><td>Less than RM25,000 </td><td>Rarely</td><td>Drive-thru</td><td>30 min to 1h</td><td>More than 3km</td><td>No</td></tr>",
                            "<tr><td>106</td><td>Male</td><td>40 and above</td><td>Employed</td><td>RM50,000 – RM100,000</td><td>Monthly</td><td>Drive-thru</td><td>30 min to 1h</td><td>More than 3km</td><td>No</td></tr>",
                            "<tr><td>107</td><td>Male</td><td>From 20 to 29</td><td>Student</td><td>Less than RM25,000 </td><td>Rarely</td><td>Take Away</td><td>Below 30 minutes</td><td>More than 3km</td><td>No</td></tr>",
                            "<tr><td>110</td><td>Male</td><td>From 20 to 29</td><td>Student</td><td>Less than RM25,000 </td><td>Rarely</td><td>Dine in</td><td>Below 30 minutes</td><td>More than 3km</td><td>No</td></tr>",
                            "<tr><td>111</td><td>Male</td><td>From 20 to 29</td><td>Student</td><td>Less than RM25,000 </td><td>Rarely</td><td>Take Away</td><td>Below 30 minutes</td><td>More than 3km</td><td>No</td></tr>",
                            "<tr><td>112</td><td>Female</td><td>From 20 to 29</td><td>Employed</td><td>Less than RM25,000 </td><td>Monthly</td><td>Take Away</td><td>Below 30 minutes</td><td>More than 3km</td><td>No</td></tr>",
                            "<tr><td>114</td><td>Female</td><td>Below 20</td><td>Student</td><td>Less than RM25,000 </td><td>Rarely</td><td>Take Away</td><td>Below 30 minutes</td><td>More than 3km</td><td>No</td></tr>",
                            "<tr><td>115</td><td>Male</td><td>40 and above</td><td>Self-Employed</td><td>RM25,000 – RM50,000</td><td>Rarely</td><td>Dine in</td><td>30 min to 1h</td><td>More than 3km</td><td>No</td></tr>",
                            "<tr><td>116</td><td>Male</td><td>Below 20</td><td>Student</td><td>Less than RM25,000 </td><td>Daily</td><td>Take Away</td><td>Below 30 minutes</td><td>More than 3km</td><td>No</td></tr>",
                            "<tr><td>117</td><td>Male</td><td>From 30 to 39</td><td>Student</td><td>Less than RM25,000 </td><td>Monthly</td><td>Dine in</td><td>1h to 2h</td><td>More than 3km</td><td>No</td></tr>",
                            "<tr><td>118</td><td>Male</td><td>40 and above</td><td>Self-Employed</td><td>RM25,000 – RM50,000</td><td>Monthly</td><td>Dine in</td><td>1h to 2h</td><td>1km to 3km</td><td>Yes</td></tr>",
                            "<tr><td>119</td><td>Male</td><td>From 20 to 29</td><td>Employed</td><td>Less than RM25,000 </td><td>Monthly</td><td>Dine in</td><td>1h to 2h</td><td>1km to 3km</td><td>Yes</td></tr>",
                            "<tr><td>120</td><td>Male</td><td>From 20 to 29</td><td>Student</td><td>Less than RM25,000 </td><td>Rarely</td><td>Dine in</td><td>30 min to 1h</td><td>1km to 3km</td><td>No</td></tr>",
                            "<tr><td>121</td><td>Female</td><td>From 20 to 29</td><td>Employed</td><td>Less than RM25,000 </td><td>Rarely</td><td>Take Away</td><td>Below 30 minutes</td><td>Within 1km</td><td>No</td></tr>",
                            "<tr><td>122</td><td>Male</td><td>From 20 to 29</td><td>Employed</td><td>RM50,000 – RM100,000</td><td>Rarely</td><td>Dine in</td><td>30 min to 1h</td><td>1km to 3km</td><td>No</td></tr>",
                            "</table>"
                        ]
                    }
                }
            ],
            "execution_count": 3
        }
    ]
}