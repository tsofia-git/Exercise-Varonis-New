
## Configurations with a security impact

### Part 1:

There are configuration methods and standards with security impact established to make the digital environment more secure and protect information from security threats and vulnerabilities.

This README provides a list of security configurations that affect users or repositories, each configuration includes details on how to automatically detect and remedy these configurations. Additionally, each configuration is associated with a compatibility category from NIST.

### 1. Two-Factor Authentication (2FA)
#### Impact:
2FA affects the security of users and repositories by adding another layer of authentication to the system. 
Instead of normal login processes, the 2FA layer requires the user to provide another authentication method, such as a one-time code, an authentication app, or a single key
It decreases the scope of vulnerability of unauthorized access.
#### Automated Detection and Fix:
Implement automated checks to verify 2FA settings for repository access, and automatically prompt users to enable MFA if not configured correctly.
#### NIST Compliance Category:
Identification and Authentication.


### 2. Role-Based Access Control (RBAC):
#### Impact:
Limits system access to authorized users based on their roles in the organization, only authorized individuals have the necessary permissions to view, edit, or manage specific repositories.
#### Automated Detection and Fix:
Implementation of automated tools and scripts that regularly check access privileges and roles assigned to users. By monitoring changes in privileges and roles, inconsistencies or unauthorized access can be identified and corrected immediately. In addition, GitHub offers features such as audit logs and integrations with continuous monitoring tools that can help track and manage access control effectively.
#### NIST Compliance Category:
Access Control.


### 3. Location-Based Access Control
#### Impact:
Restricts access to resources based on the geographic location of the user or device attempting to access them, and allows administrators to set rules that limit access to certain repositories or actions based on the user's physical location.
#### Automated Detection and Fix:
Using an automated tool that can detect and compare in real-time the user's location, suspicious access attempts from unauthorized locations can trigger alerts or automated responses, such as blocking access or requiring additional authentication steps to verify the user's identity.
#### NIST Compliance Category:
Access Control.


### 4. Device-Based Access Control
#### Impact:
This type of access control affects users and repositories by adding a layer of security that ensures the access is only granted from approved devices, by authenticating users based on their devices
#### Automated Detection and Fix:
Implementation of solutions that monitor and analyze information about the device during authentication attempts. If a user tries to access from an unrecognized or authorized device, you can activate automatic alerts, request additional authentication steps, or block access until the user's identity is verified. In addition, organizations can implement device management tools that integrate with access control systems to effectively enforce device-based restrictions.
#### NIST Compliance Category:
Access Control.


### 5. Contingency planning - permanent backups of a repository to a secure off-site location
#### Effect:
Ensures data integrity and availability in the event of data loss or system failure.
#### Automatic detection and repair:
Using automated backup monitoring tools to verify backup schedules and transfer data to offsite locations. and automatic activation of backup processes if scheduled backups are missed.
#### NIST Compliance Category:
contingency planning.



### Part 2 - Two-Factor Authentication (2FA) in Simple Terms:
**Two-factor authentication (2FA)** is like having a double lock on your digital door. When you want to access your online accounts, in addition to your password (the first lock), you also need a second piece of information, like a code sent to your phone. This extra step adds another layer of security to protect your accounts from unauthorized access.

* The best practice is to enable Two-Factor Authentication on your online accounts. This ensures that even if someone gets hold of your password, they still need the second factor (like your phone) to access your account, adding an extra layer of security.

* Enabling Two-Factor Authentication means that in addition to entering your password when logging into your account, you will also need to provide a second piece of information that only you have access to, such as a code sent to your phone or generated by an authentication app.

* If Two-Factor Authentication is not enabled, there is a higher risk of unauthorized access to your account if someone gains access to your password. Without this extra layer of security, hackers or anyone else could potentially log in to your account and access sensitive information or perform actions on your behalf.

* To enable 2FA manually, you would typically go to your account settings, look for the Two-Factor Authentication option, and follow the steps to set it up. To work around risks without 2FA, you can regularly update your password, use unique and strong passwords for each account, and be cautious of phishing attempts.

* Enabling Two-Factor Authentication on GitHub adds an extra layer of security to your account. While it may require an additional step during login, it significantly reduces the risk of unauthorized access, especially considering the sensitive code and data stored on GitHub repositories.

* Here are some attack techniques that are often related to the configuration of 2FA:

1. **Phishing (T1566.001):**
   - **Explanation:** Phishing attacks are commonly used to trick individuals into providing their login credentials, including the second factor used in 2FA. Attackers may send deceptive emails or messages that appear to be from a legitimate source, prompting users to enter both their password and the 2FA code into a fake website controlled by the attacker. By compromising both factors, attackers can gain unauthorized access to the victim's account.

2. **Credential Stuffing (T1110.003)**

3. **Password Spraying (T1110.004)**


### Part 3 - Setup & Usage 

[*python_code.py*] script - The python_code.py script checks the status of the configuration of Private Repositories. If it is private, it will only print its status, and if it is public, it will change the repository to private and notify it, by setting the repository as private, it can be said that only authorized users can see and contribute to the repository.

To run the script locally, you need to have Python 3.11.X installed, and you have to run the following command on Git Bash:
```shell
git clone https://github.com/tsofia-git/Exercise-Varonis-New.git
```

And the following installations commands on Terminal: 
```shell
pip install dotenv
pip install dotenv
```

Then run the script: 
```shell
python python_code.py
```

You should be notified of the status of the repository.
![image](https://github.com/tsofia-git/Exercise-Varonis-New/assets/99796311/690aedc5-b8af-4fab-978e-6e813df54e53)

#### **Caution!!! The script changes the repository to private**

