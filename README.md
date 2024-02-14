
## Configurations with a security impact

### Part 1:

There are configuration methods and standards with security impact established to make the digital environment more secure and protect information from security threats and vulnerabilities.

This README provides a list of security configurations impacting either users or repositories, each configuration includes details on how to detect and automatically fix these configurations. Additionally, each configuration is associated with a compliance category from NIST.

### 1. Two-Factor Authentication (2FA)
#### Impact:
2FA affects the security of users and repositories by adding another layer of authentication to the system. 
Instead of normal login processes, the 2FA layer requires the user to provide another authentication method, such as a one-time code, an authentication app, or a single key
It decreases the scope of vulnerability of unauthorized access
#### Automated Detection and Fix:
Implement automated checks to verify 2FA settings for repository access, automatically prompt users to enable MFA if not configured correctly.
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
This type of access control affects users and repositories by adding layer of security that ensures access is only granted from approved devices. By authenticating users based on their devices
#### Automated Detection and Fix:
Implementation of solutions that monitor and analyze information about the device during authentication attempts. If a user tries to access from an unrecognized or authorized device, you can activate automatic alerts, request additional authentication steps, or block access until the user's identity is verified. In addition, organizations can implement device management tools that integrate with access control systems to effectively enforce device-based restrictions.
#### NIST Compliance Category:
Access Control.


### 5. Contingency Planning - Regularly scheduled repository backups to a secure offsite location
#### Impact:
Ensures data integrity and availability in the event of data loss or system failure.
#### Automated Detection and Fix:
Utilize automated backup monitoring tools to verify backup schedules and data transfer to offsite locations. Automatically trigger backup processes if scheduled backups are missed.
#### NIST Compliance Category:
Contingency Planning.



### Part 2 - Two-Factor Authentication (2FA) in Simple Terms:
T**wo-factor authentication (2FA)** is like having a double lock on your digital door. When you want to access your online accounts, in addition to your password (the first lock), you also need a second piece of information, like a code sent to your phone. This extra step adds another layer of security to protect your accounts from unauthorized access.

* It is best practice to enable Two-Factor Authentication on your online accounts. This ensures that even if someone gets hold of your password, they still need the second factor (like your phone) to access your account, adding an extra layer of security.

* Enabling Two-Factor Authentication means that in addition to entering your password when logging into your account, you will also need to provide a second piece of information that only you have access to, such as a code sent to your phone or generated by an authentication app.

* If Two-Factor Authentication is not enabled, there is a higher risk of unauthorized access to your account if someone gains access to your password. Without this extra layer of security, hackers or anyone else could potentially log in to your account and access sensitive information or perform actions on your behalf.
