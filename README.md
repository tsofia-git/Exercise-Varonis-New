
## configurations with a security impact

There are configuration methods and standards with security impact established to make the digital environment more secure and protect information from security threats and vulnerabilities.

This README provides a list of security configurations impacting either users or repositories, each configuration includes details on how to detect and automatically fix these configurations. Additionally, each configuration is associated with a compliance category from NIST.

### 1. Two-Factor Authentication (2FA)
#### Impact:
2FA affects the security of users and repositories by adding another layer of authentication to the system. 
Instead of normal login processes, the 2FA layer requires the user to provide another authentication method, such as a one-time code, an authentication app, or a single key
It decreases the scope of vulnerability of unauthorized access
#### Automated Detection and Fix:
Implement an automated system to enforce 2FA for all users.
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
Using an automated tool that can detect and compare in real time the user's location, suspicious access attempts from unauthorized locations can trigger alerts or automated responses, such as blocking access or requiring additional authentication steps to verify the user's identity.
#### NIST Compliance Category:
Access Control.


### 4. Device-Based Access Control
#### Impact:
This type of access control affects users and repositories by adding an additional layer of security that ensures access is only granted from approved devices. By authenticating users based on their devices
#### Automated Detection and Fix:
Implementation of solutions that monitor and analyze information about the device during authentication attempts. If a user tries to access from an unrecognized or authorized device, you can activate automatic alerts, request additional authentication steps, or block access until the user's identity is verified. In addition, organizations can implement device management tools that integrate with access control systems to effectively enforce device-based restrictions.
###\3 NIST Compliance Category:
Access Control.


### 5. Contingency Planning Configuration
#### Impact:
Defines a backup and recovery plan for repositories in case of unexpected incidents.
#### Automated Detection and Fix:
Automated tools can monitor the repository's health and execute backup and recovery processes as needed.
#### NIST Compliance Category:
Contingency Planning


