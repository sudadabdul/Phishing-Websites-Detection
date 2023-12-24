# **Phishing-Websites-Dataset-Inventory**

---

## **Data Set Information**

[Phishing Websites Features](https://core.ac.uk/download/pdf/30732240.pdf)

This dataset contains 11055 instances with 31 attributes (30 predictive and 1 goal field) collected mainly from: PhishTank archive, MillerSmiles archive, Google's searching operators.

1. **Address Bar based Features:**

    - **having_IP_Address**: Presence of an IP address in the URL. (-1 indicates absence, 1 indicates presence)
    - **URL_Length**: Length of the URL. (1: long, 0: average, -1: short)
    - **Shortening_Service**: Use of URL shortening services like TinyURL. (1: yes, -1: no)
    - **having_At_Symbol**: Presence of "@" symbol in the URL. (1: yes, -1: no)
    - **double_slash_redirecting**: Presence of double slashes in the URL. (-1: no, 1: yes)
    - **Prefix_Suffix**: Presence of prefix or suffix separated by a dash in the domain. (-1: no, 1: yes)
    - **having_Sub_Domain**: Presence of subdomains in the URL. (-1: no, 0: neutral, 1: yes)
    - **SSLfinal_State**: SSL final state of the website. (-1: insecure, 1: secure, 0: unknown)
    - **Domain_registeration_length**: Length of domain registration. (-1: short, 1: long)
    - **Favicon**: Loading of favicon from an external domain. (1: yes, -1: no)
    - **port**: Use of a non-standard port. (1: yes, -1: no)
    - **HTTPS_token**: Presence of "HTTPS" token in the domain part of the URL. (-1: no, 1: yes)
2. **Abnormal Based Features:**
    - **Request_URL**: Examination of external objects (images, videos) loaded from another domain. (1: legitimate, -1: phishing)
    - **URL_of_Anchor**: Analysis of anchor elements in the HTML source code. (-1: phishing, 0: neutral, 1: legitimate)
    - **Links_in_tags**: Analysis of links in meta, script, and link tags. (1: legitimate, -1: phishing, 0: neutral)
    - **SFH**: Analysis of Server Form Handler (SFH) in the HTML source code. (-1: phishing, 1: legitimate, 0: suspicious)
    - **Submitting_to_email**: Submission of information to an email. (-1: no, 1: yes)
    - **Abnormal_URL**: Examination of abnormal URLs from the WHOIS database. (-1: legitimate, 1: phishing)
3. **HTML and JavaScript based Features:**
    - **Redirect**: Number of redirects on a webpage. (0: no redirect, 1: redirected)
    - **on_mouseover**: Usage of JavaScript to show a fake URL in the status bar. (1: phishing, -1: legitimate)
    - **RightClick**: Disabling of the right-click function using JavaScript. (1: phishing, -1: legitimate)
    - **popUpWidnow**: Usage of pop-up windows on the webpage. (1: phishing, -1: legitimate)
    - **Iframe**: Presence of an iframe in the HTML source code. (1: phishing, -1: legitimate)
4. **Domain based Features:**
    - **age_of_domain**: Age of the domain extracted from the WHOIS database. (-1: short, 1: long)
    - **DNSRecord**: Presence of DNS records for the domain. (-1: no records, 1: records found)
    - **web_traffic**: Measurement of website popularity based on traffic. (-1: phishing, 0: unknown, 1: legitimate)
    - **Page_Rank**: PageRank value of the webpage. (-1: no PageRank, 1: PageRank present)
    - **Google_Index**: Presence of the website in Google's index. (1: indexed, -1: not indexed)
    - **Links_pointing_to_page**: Number of links pointing to the webpage. (1: legitimate, 0: neutral, -1: phishing)
    - **Statistical_report**: Presence of the website in top phishing domains or IPs based on statistical reports. (-1: not in top phishing, 1: in top phishing)
