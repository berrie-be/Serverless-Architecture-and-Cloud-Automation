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








  
