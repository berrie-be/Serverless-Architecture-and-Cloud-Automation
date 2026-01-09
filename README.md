## Assignment 1: Automated Instance Management Using AWS Lambda and Boto3   
1. EC2 Setup:  
  - Navigate to the EC2 dashboard and create two new t2.micro instances (or any other available free-tier type).  
  - Tag the first instance with a key `Action` and value `Auto-Stop`.  
    <img width="540" height="657" alt="image" src="https://github.com/user-attachments/assets/d4e63abf-6de8-4cf6-84c1-08b939c199ee" />  
    <img width="540" height="657" alt="image" src="https://github.com/user-attachments/assets/ab3c90c8-51ee-4754-a773-c7f21377b7e0" />  
     
  - Tag the second instance with a key `Action` and value `Auto-Start`.  
    <img width="540" height="657" alt="image" src="https://github.com/user-attachments/assets/d09f26a1-30c7-4b36-9852-f6be22782478" />  
    <img width="540" height="657" alt="image" src="https://github.com/user-attachments/assets/1c2a56f9-89bf-4a11-bf36-dbfb5689f561" />
      
2. Lambda IAM Role:  
  - In the IAM dashboard, create a new role for Lambda.  
  - Attach the `AmazonEC2FullAccess` policy to this role. (Note: In a real-world scenario, you would want to limit permissions for better security.)  
    <img width="2914" height="954" alt="image" src="https://github.com/user-attachments/assets/d625df00-9817-4be0-9c1f-e7d1f98ad561" />
    <img width="2932" height="1190" alt="image" src="https://github.com/user-attachments/assets/83d7d42f-bf67-48d1-b7b0-fc2ad9816e1d" />
    <img width="2928" height="1364" alt="image" src="https://github.com/user-attachments/assets/761e6a13-0a53-4bb4-80a3-4edd6ab71a4f" />
    <img width="1668" height="846" alt="image" src="https://github.com/user-attachments/assets/fdedff30-7506-4e0d-b6d7-dc4e485088d1" />

3. Lambda Function:  
  - Navigate to the Lambda dashboard and create a new function.  
  - Choose Python 3.x as the runtime.  
  - Assign the IAM role created in the previous step.  
  - Write the Boto3 Python script to:  
    1. Initialize a boto3 EC2 client.  
    2. Describe instances with `Auto-Stop` and `Auto-Start` tags.  
    3. Stop the `Auto-Stop` instances and start the `Auto-Start` instances.  
    4. Print instance IDs that were affected for logging purposes.
       <img width="1648" height="1064" alt="image" src="https://github.com/user-attachments/assets/11b54d54-a247-4b62-8922-a658f482899d" />  
       <img width="1592" height="942" alt="image" src="https://github.com/user-attachments/assets/0e5d3ad3-acf5-49bd-b491-2e9faf3f1d47" />
       <img width="2400" height="924" alt="image" src="https://github.com/user-attachments/assets/f8f08956-a22b-4187-9bf1-372d9e51e03d" />
       <img width="2406" height="1212" alt="image" src="https://github.com/user-attachments/assets/dce254e6-44e7-4054-bb2e-4cfdc9191ace" />
   
4. Testing:  
  - Manually invoke the Lambda function.  
  - Confirm that the instance tagged `Auto-Stop` stops and the one tagged `Auto-Start` starts.  
       <img width="2366" height="1068" alt="image" src="https://github.com/user-attachments/assets/7f80d2b8-7076-46ac-a097-171d2a53e0bb" />

## Assignment 2: Automated S3 Bucket Cleanup Using AWS Lambda and Boto3  
1. S3 Setup:  
  - Navigate to the S3 dashboard and create a new bucket.  
  - Upload multiple files to this bucket, ensuring that some files are older than 30 days (you may need to adjust your system's date temporarily for this or use old files).
    <img width="1646" height="1272" alt="image" src="https://github.com/user-attachments/assets/57f7969b-3cc6-4651-ba63-bbf48dd36c09" />
    <img width="834" height="424" alt="image" src="https://github.com/user-attachments/assets/b4390a2f-9f6b-4cb0-b577-80fcd2b97ff5" />
    <img width="1656" height="412" alt="image" src="https://github.com/user-attachments/assets/234438a7-8f2e-4068-80bd-c2143309709f" />
    <img width="1660" height="832" alt="image" src="https://github.com/user-attachments/assets/91d1f663-2f7c-4368-b630-d30ce13c301c" />

    Upload files and update the metadata of the file to before 30 days using AWS CLI  
    <img width="704" height="657" alt="image" src="https://github.com/user-attachments/assets/370dacae-e83c-40c8-802a-bc027d3255d0" />
    <img width="823" height="259" alt="image" src="https://github.com/user-attachments/assets/28f0af0a-166e-4edf-a8ee-c526dff5bfbe" />  

2. Lambda IAM Role:  
  - In the IAM dashboard, create a new role for Lambda.  
  - Attach the `AmazonS3FullAccess` policy to this role. (Note: For enhanced security in real-world scenarios, use more restrictive permissions.)
    <img width="2932" height="504" alt="image" src="https://github.com/user-attachments/assets/11b4cf8f-c641-4b72-b314-de976a076db1" />
    <img width="2924" height="1312" alt="image" src="https://github.com/user-attachments/assets/00826c38-b0b2-4932-a44f-4d7be730bbec" />  

3. Lambda Function:  
  - Navigate to the Lambda dashboard and create a new function.  
  - Choose Python 3.x as the runtime.  
  - Assign the IAM role created in the previous step.
    <img width="869" height="537" alt="image" src="https://github.com/user-attachments/assets/c7a84394-925c-4f5c-9914-9acd15929217" />  
    <img width="815" height="552" alt="image" src="https://github.com/user-attachments/assets/d9659eac-6e01-4db4-8cf5-1bec7ab3fb0b" />  
    <img width="1209" height="594" alt="image" src="https://github.com/user-attachments/assets/b835d979-f6c4-429c-8419-71417dc94494" />  

  - Write the Boto3 Python script to:  
    1. Initialize a boto3 S3 client.  
    2. List objects in the specified bucket.  
    3. Delete objects older than 30 days.  
    4. Print the names of deleted objects for logging purposes.  
       <img width="425" height="356" alt="image" src="https://github.com/user-attachments/assets/1f720130-1761-4d07-b890-67866a156919" />

4. Manual Invocation:  
  - After saving your function, manually trigger it.  
  - Go to the S3 dashboard and confirm that only files newer than 30 days remain.
    <img width="805" height="575" alt="image" src="https://github.com/user-attachments/assets/5bb4d2f7-152c-40ca-bfdf-fe927a4db26f" />
    <img width="817" height="199" alt="image" src="https://github.com/user-attachments/assets/6c4e68ba-6c33-4ff7-a5b3-9a1ba8a3a469" />  


    


         






 
        









  
