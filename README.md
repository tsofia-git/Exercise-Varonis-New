
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


