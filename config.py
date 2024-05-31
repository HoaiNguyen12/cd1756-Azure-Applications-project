import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'azureudacity'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'zasbZ4ivqSzH/EEpElERJ8caodw8MoQQfC7O6/GX++cxN4HeHsDGhkMpnPuL4TRLf7IHPkQ9vqa7+AStCwcLkA=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'tcp:azure-udacity.database.windows.net,1433'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'azure-udacity-prj1'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'dbAdmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or '1qaz!QAZ'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc:///?odbc_connect=Driver={ODBC Driver 17 for SQL Server};Server=' + SQL_SERVER + ';Database=' + SQL_DATABASE + ';Uid=' + SQL_USER_NAME + ';Pwd=' + SQL_PASSWORD + ';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "rpQ8Q~OKzWaGp_B.~~rfqq673Bx7dI9ce~V~maoo"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "8720cd6f-3eec-4aab-b22e-4624cd5547d4"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session