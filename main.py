import boto3

client = boto3.client("ses", region_name="ap-south-1")

# store the content of cetmail.html in a variable
with open("span.html", "r", encoding="utf8") as f:
    template = f.read()

# get email_list from a csv file
with open("recruitments.csv", "r", encoding="utf8") as f:
    email_list = f.read().splitlines()

for cnt, email in enumerate(email_list):
    try:
        response = client.send_email(
            Destination={
                "ToAddresses": [email],
            },
            Message={
                "Body": {
                    "Html": {
                        "Charset": "UTF-8",
                        "Data": template,
                    },
                    "Text": {
                        "Charset": "UTF-8",
                        "Data": "This is for those who cannot read HTML.",
                    },
                },
                "Subject": {
                    "Charset": "UTF-8",
                    "Data": "Recruitments' 22: CodeChef-VIT",
                },
            },
            Source="CodeChef-VIT <noreply@codechefvit.com>",
        )
        print(cnt + 1, email)
    except Exception as e:
        print(e)
        # append the email into a fail.csv file
        with open("fail.csv", "a", encoding="utf8") as f:
            f.write(email + "<br>")
