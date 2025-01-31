:orphan: .. NOT DELETE: Avoid warning about document not being included in any toctree

Installation
============

**Prerequisite**

- Python 3.8.10 ([installer](https://www.python.org/ftp/python/3.8.10/python-3.8.10-amd64.exe))
- GAMS 45.7 ([installer](https://d37drm4t2jghv5.cloudfront.net/distributions/45.7.0/windows/windows_x64_64.exe))
- Git ([installer](https://git-scm.com/download/win))
- IDE (e.g., [VS Code](https://code.visualstudio.com/docs/?dv=win))
- Tableau (executable given with the license for the software Tableau Desktop). The example of Tableau file is located in `cactus2postgresql/Cactus_Tableau.twb`
- PostgreSQL (WARNING YOU NEED ADMIN RIGHTS) ([installer](https://www.enterprisedb.com/postgresql-tutorial-resources-training-2?uuid=d732dc13-c15a-484b-b783-307823940a11&campaignId=Product_Trial_PostgreSQL_16)). Please note that at some point a password will be asked. First, note this password carefully, and then please use a simple password without any special characters (as it’s only for a local database there is no need to put a very robust password). Indeed, you will see that later on such password will be asked and putting special characters will create some issues. So please, use a simple password without special characters.
  - For your information, installing PostgreSQL will also install pgAdmin, which will be used to create and manage your PostgreSQL databases.
- Request the rights to Cactus’ repository ([https://github.tools.digital.engie.com/GEM3mv/Cactus](https://github.tools.digital.engie.com/GEM3mv/Cactus)). Ping Raphaël LASRY, Paul BARBERI or Roman SIMCIK for instance.

**Installation Steps**

1. **Install Python 3.8.10**:
   - Download the installer from the link above.
   - Run the installer and follow the instructions.

2. **Install GAMS 45.7**:
   - Download the installer from the link above.
   - Run the installer and follow the instructions.

3. **Install Git**:
   - Download the installer from the link above.
   - Run the installer and follow the instructions.

4. **Install IDE (e.g., VS Code)**:
   - Download the installer from the link above.
   - Run the installer and follow the instructions.

5. **Install Tableau**:
   - Use the executable provided with the license for Tableau Desktop.
   - The example of Tableau file is located in `cactus2postgresql/Cactus_Tableau.twb`.

6. **Install PostgreSQL**:
   - Download the installer from the link above.
   - Run the installer and follow the instructions.
   - Note the password carefully and use a simple password without special characters.

7. **Request Access to Cactus Repository**:
   - Request access to the repository from the link above.
   - Contact Raphaël LASRY, Paul BARBERI, or Roman SIMCIK for access.

**Testing the Installation**

1. **Edit the Configuration File**:
   - Edit the file `config.json` located in the `cactus2postgresql` directory with the information of your local database.

2. **Activate Your Environment**:
   - Activate your environment using the command: `workon cactus38`.

3. **Run the Test Command**:
   - Navigate to the root of the Cactus repository (where the `main.py` file is located).
   - Run the following command:
     ```sh
     python main.py -d "documentation/installations" -i "example.xlsx" -c "cats.xml" -o "output.xlsx" --e
     ```

4. **Import the File**:
   - When the run is done, a pop-up window should appear.
   - Click on "Start importing file".

5. **Verify the Results in Tableau**:
   - Open Tableau.
   - Link the newly created table and visualize the results.
   - If everything went well, in the balance CAL sheet you should see the following table.

**Additional Steps**

- Drag & Drop the table (e.g., `raph_test`) that is on the left in the Table part to the Migrated Data. (Be careful, here you have to place the new table on top of the old one). At this step of the installation process, you shouldn’t have yet a table. Please come back to this step just after testing a run.