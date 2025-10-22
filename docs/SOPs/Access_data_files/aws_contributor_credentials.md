---
layout: default
title: AWS User for Contributors
parent: Access data files
grand_parent: SOPs
has_children: false
nav_order: 1
---

# AWS User for Contributors

In order for a contributor to upload their data, they would need their own AWS user that is assigned to the hca-contributor group. 
A request for an account should be files as [a new ticket](https://github.com/ebi-ait/hca-ebi-wrangler-central/issues/new?assignees=&labels=operations&template=new-contributor-account.md&title=contributor+account+for%3A+%3Ccontributor-name%3E) for the ingest team. The board is monitored regularly so the new ticket would be picked up within the day.
In order for a contributor to upload their data, they would need their own AWS user that is assigned to the hca-contributor group.

A request for an account should be filed as [a new ticket](https://github.com/ebi-ait/hca-ebi-wrangler-central/issues/new?assignees=&labels=operations&template=new-contributor-account.md&title=contributor+account+for%3A+%3Ccontributor-name%3E) for the ingest team. The board is monitored regularly so the new ticket would be picked up within the day.

_**This is done by a team member with a developer role.**_

1. Create an AWS user
   
   Use the name part of the email address for the account name.
  
```shell
# to add user as a contributor
read -p "enter username: " contributor_username
aws iam create-user --user-name $contributor_username --tags Key=project,Value=hca Key=owner,Value=tburdett Key=service,Value=ait
aws iam add-user-to-group --group hca-contributor --user-name $contributor_username
# generate secrets 
aws iam create-access-key --user-name $contributor_username > ${contributor_username}.txt
```

2. The credentials json output into a `<username>-access-keys.txt` file. Example:
```json
{
    "AccessKey": {
        "UserName": "walter.white",
        "AccessKeyId": "access-key-id",
        "Status": "Active",
        "SecretAccessKey": "secret-access-key",
        "CreateDate": "2022-03-10T16:35:07+00:00"
    }
}
```

3. Compress the file with password. The following steps works for mac os.
```bash
zip -er ${$contributor_username}-access-keys.zip ${$contributor_username}-access-keys.txt
```
You will be prompted to input a password. You could use any password generator.
```
Enter password:
Verify password:
  adding: walter.white-access.txt (deflated 30%)

```

4. Compose an email and attach the `.zip` file

Subject: `AWS access keys for hca-util tool`

To: `wrangler.email@domain.org`

Message:
> Dear < Contributor Name >
> 
> Attached at the end of the email you will find a zip file with the credentials you need for the hca-util tool to upload your data. I will send you a separate email for the password of the zip file.
>
> < Wrangler Name > will provide you with further details on how to continue with the submission.
> 
> 
> Best regards
> 
> < Your Name >

5. Compose a second email containing the `.zip` file password

>Dear < Contributor Name >
> 
>The password to open the zip file is: < password >
> 
> 
> Best Regards
> 
> < Your Name > 
   
