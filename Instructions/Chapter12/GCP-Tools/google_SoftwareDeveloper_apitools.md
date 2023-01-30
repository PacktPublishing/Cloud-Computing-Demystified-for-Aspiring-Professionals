# Instructions

## Prerequisite tasks

1. Review instructions located in chapter 12 Utilizing Management API Tools for Agility
> Note: After reviewing and complying with all required prerequisites return to this file and continue to the next task.

## Task 1: Learn the Google Cloud SDK essentials.

1.	Sign in to the [Google Cloud Console](https://console.cloud.google.com/)

3.	In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

5.	Make sure that billing is enabled for your Google Cloud project.

> **Note**: Helpful tips and tricks are in the book in chapter 12 Utilizing Management API Tools for Agility.

4.	Enable Google Cloud API.

5.	Go to the Google Cloud SDK web page: https://cloud.google.com/sdk/.

7.	Review the Google Cloud SDK page and its key features.

9.	Select Python from the available client libraries.

11.	On the Python Cloud Client Libraries page, search for and select Google Cloud Storage.

13.	Select Bucket from the API documentation.

15.	Review how to use buckets programmatically

![image](https://user-images.githubusercontent.com/61672321/215555228-420a3370-72ee-4b5b-b26c-ebfd1c72b5e7.png)

11.	Once installed, you can start developing.

13. Review the following figure, which displays the copy_blob() function.

![image](https://user-images.githubusercontent.com/61672321/215555501-3ab254ca-e84c-441e-ad51-01a2bd36acf7.png)

14. In the google cloud console select and activate cloud shell.

15. In the cloud shell terminal type the following commands:

```
export LOCATION=us-west1
```
```
gsutil mb -l $LOCATION gs:$DEVSHELL_PROJECT_ID """ Creates a storage bucket and generates a unique name using your project identifier """
```
16. Select, Open Editor to access the editor section in cloud shell.

17. Select, File, and then select New File. Select File and then select Save As.

18. Type a name replacing the name Untitled-1. Here is an example: storageSDK.py. The file name requires " .py " at the end.

19. Enter the following lines of code. Note: The file indentation format is required.

```
""" This function lists Google Cloud storage buckets in your current project. """
from google.cloud import storage
""" Importing SDK libary modules containing functions """

def getstorage_buckets(self):
    """ custom function """
    storageSDK_client = storage.Client()
    storageBuckets = storageSDK_client.list_buckets()

    for variablebucket in storageBuckets:
        print(variablebucket.name)
```
> Note: Google Cloud SDK for python is installed in Google Cloud Shell by default.

