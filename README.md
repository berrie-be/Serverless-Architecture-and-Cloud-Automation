## Assignment 1: Automated Instance Management Using AWS Lambda and Boto3   
### Objective: In this assignment, you will gain hands-on experience with AWS Lambda and Boto3, Amazon's SDK for Python. You will create a Lambda function that will automatically manage EC2 instances based on their tags.
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
### Objective: To gain experience with AWS Lambda and Boto3 by creating a Lambda function that will automatically clean up old files in an S3 bucket.

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

## Assignment 3: Monitor Unencrypted S3 Buckets Using AWS Lambda and Boto3  
### Objective: To enhance your AWS security posture by setting up a Lambda function that detects any S3 bucket without server-side encryption.  

1. S3 Setup:  
  - Navigate to the S3 dashboard and create a few buckets. Ensure that a couple of them don't have server-side encryption enabled.
    As by default, encryption is enabled for S3 now, I have chosen two different enceyptions - one with KMS and two with Amazon S3 managed keys
    <img width="1634" height="1170" alt="image" src="https://github.com/user-attachments/assets/b13fb142-87bb-4793-b4c9-47cbf74988b6" />  
    <img width="1628" height="840" alt="image" src="https://github.com/user-attachments/assets/814255c7-6103-4d58-a35a-9318abcc58cb" />  
    <img width="1626" height="1242" alt="image" src="https://github.com/user-attachments/assets/37e15329-d2fd-40f5-9299-ed410d74b110" />  
    <img width="1628" height="1046" alt="image" src="https://github.com/user-attachments/assets/79a75da1-5703-4acb-8728-4807e8c582b6" />  
    <img width="1636" height="1242" alt="image" src="https://github.com/user-attachments/assets/2b82e6fa-c6ad-4a3d-b7d3-53bc454fa71c" />  
    <img width="1628" height="848" alt="image" src="https://github.com/user-attachments/assets/5be788ec-8cc9-43d3-a985-b7889eee5021" />  

    <img width="1074" height="262" alt="image" src="https://github.com/user-attachments/assets/bd61316a-5473-443d-847f-b7fd8586dd90" />  

2. Lambda IAM Role:  
  - In the IAM dashboard, create a new role for Lambda.  
  - Attach the `AmazonS3ReadOnlyAccess` policy to this role.  
    <img width="1464" height="579" alt="image" src="https://github.com/user-attachments/assets/5919b8f3-88b5-42f5-9ad9-9cd0dcfad89a" />    
    <img width="1460" height="368" alt="image" src="https://github.com/user-attachments/assets/d9499ada-e0c0-4988-8ff4-660c5e157c5e" />  
    <img width="1469" height="654" alt="image" src="https://github.com/user-attachments/assets/7555f64d-f0fb-489c-8adc-7508b4f958f9" />  
    <img width="818" height="414" alt="image" src="https://github.com/user-attachments/assets/e1ed8c3b-6d58-4cfd-b0cd-faef4e5ea1dd" />  

3. Lambda Function:  
  - Navigate to the Lambda dashboard and create a new function.  
  - Choose Python 3.x as the runtime.  
  - Assign the IAM role created in the previous step.  
    <img width="825" height="535" alt="image" src="https://github.com/user-attachments/assets/359bd306-a07f-4420-8784-b9bfb99feed4" />  
    <img width="809" height="439" alt="image" src="https://github.com/user-attachments/assets/7074c5b1-4dd1-41af-9f53-4c90b8435a85" />  
    <img width="805" height="404" alt="image" src="https://github.com/user-attachments/assets/a8630ded-7478-4a5d-a2b9-06606354f42c" />  
      
  - Write the Boto3 Python script to:  
    1. Initialize a boto3 S3 client.  
    2. List all S3 buckets.  
    3. Detect buckets without server-side encryption.  
    4. Print the names of unencrypted buckets for logging purposes.  
       <img width="554" height="345" alt="image" src="https://github.com/user-attachments/assets/02c21c33-619b-4cc3-a2c8-daa21d4706f7" />

4. Manual Invocation:
  - After saving your function, manually trigger it.
  - Review the Lambda logs to identify the buckets without server-side encryption.
    <img width="802" height="550" alt="image" src="https://github.com/user-attachments/assets/77aa0c24-b2c8-4246-9784-b4cf202c80da" />

## Assignment 4: Automatic EBS Snapshot and Cleanup Using AWS Lambda and Boto3  
### Objective: To automate the backup process for your EBS volumes and ensure that backups older than a specified retention period are cleaned up to save costs.  
    
1. EBS Setup:  
  - Navigate to the EC2 dashboard and identify or create an EBS volume you wish to back up.
  - Note down the volume ID.
    <img width="1263" height="467" alt="image" src="https://github.com/user-attachments/assets/fd01b210-cf60-4389-90b7-7a90d673693f" />
    

2. Lambda IAM Role:
  - In the IAM dashboard, create a new role for Lambda.
  - Attach policies that allow Lambda to create EBS snapshots and delete them (`AmazonEC2FullAccess` for simplicity, but be more restrictive in real-world scenarios).
    <img width="824" height="410" alt="image" src="https://github.com/user-attachments/assets/d9a84074-7d39-4104-b746-688f61e7a86e" />


3. Lambda Function:  
  - Navigate to the Lambda dashboard and create a new function.  
  - Choose Python 3.x as the runtime.  
  - Assign the IAM role created in the previous step.  
    <img width="818" height="570" alt="image" src="https://github.com/user-attachments/assets/a073b077-29ff-40c8-9925-4fd478fa1e5b" />  
    <img width="1614" height="816" alt="image" src="https://github.com/user-attachments/assets/ade88350-1078-4202-9691-95b6747c5cee" />  
    <img width="809" height="438" alt="image" src="https://github.com/user-attachments/assets/a3a93583-d678-4803-9950-741b4f96923e" />    

  - Write the Boto3 Python script to:
    1. Initialize a boto3 EC2 client.
    2. Create a snapshot for the specified EBS volume.
    3. List snapshots and delete those older than 30 days.
    4. Print the IDs of the created and deleted snapshots for logging purposes.
       As I cannot get any snapshot which is older than 30 days, I will attach the screenshots of the result I get if I delete the snapsots which were created just today and verify           the code how it works only for checking.
       There is one snapshot which is already created for the volume and one will be created during this code. And the code will delete the snapshot which was created earlier.
   
       Python Code  
       <img width="1194" height="1328" alt="image" src="https://github.com/user-attachments/assets/eb36ce94-1c6d-4b1d-bb45-d4d229287fb0" />
         
       Output  
       <img width="1036" height="269" alt="image" src="https://github.com/user-attachments/assets/b64c43f8-bd45-476a-a15d-4a6b0c2c427d" />

       I have modified the code according to the assignment and put in the Lambda Function.  
       <img width="1196" height="1078" alt="image" src="https://github.com/user-attachments/assets/e2720074-0497-4093-9b01-c2fd18bee24e" />  
       <img width="1067" height="528" alt="image" src="https://github.com/user-attachments/assets/aaab1dd3-e6ab-4bd5-ae30-20c24699525d" />

4. Event Source (Bonus):  
  - Attach an event source, like Amazon CloudWatch Events, to trigger the Lambda function at your desired backup frequency (e.g., every week).  
    <img width="966" height="56" alt="image" src="https://github.com/user-attachments/assets/b9edb0ad-e166-47ec-84b8-0e209d8cd7ec" />
    <img width="1230" height="444" alt="image" src="https://github.com/user-attachments/assets/57653098-98e7-46e4-8b5a-45480026b395" />
    <img width="583" height="162" alt="image" src="https://github.com/user-attachments/assets/e7dca9a5-5047-4912-a4cb-4f6deb174057" />

    Now we will add a Trigger to our lambda function which will run the lambda function every Sunday 12.30AM  
    <img width="820" height="391" alt="image" src="https://github.com/user-attachments/assets/6f120655-e2bd-4ece-8318-6e686004726c" />
    
    <img width="310" height="128" alt="image" src="https://github.com/user-attachments/assets/f1c504a2-cd85-4dce-83d6-a7d26d41ba76" />

5. Manual Invocation:  
  - After saving your function, either manually trigger it or wait for the scheduled event.  
    First line proves that the function got triggered at 11th Jan 12.30 AM IST  
    <img width="779" height="385" alt="image" src="https://github.com/user-attachments/assets/defa7a7a-aa3d-48ec-9d8b-fdb458279c66" />
    <img width="1552" height="282" alt="image" src="https://github.com/user-attachments/assets/b867cebe-c24a-467b-a05c-acbbf2fed8a9" />  




    

 





    














    



    


         






 
        









  
