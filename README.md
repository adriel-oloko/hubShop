DATA
***********
#TITLE: Online shop (Hub)
#AUTHOR: Adriel (Adrielloks)
#CLIENT: Worldwide
#START DATE: Nil
#END DATE:
#OFFSHOOT: JJ
#LICENSCE: --
#FILE AMOUNT:
#FILE SIZE(approx.):

GOAL: To make an online drop shipping website site similar to piopaul.

FILE STRUCTURE
***********
Hub
|
|_hub.py
|
|_css____
|        |_font-awesome.min.css
|        |_navbar.css
|        |_style.css
|        |_toolbar.css
|
|
|_images_
|        |_*.jpeg
|        |_*.jpg
|        |_*.png
|
|
|_js____
|       |_navbar.js
|       |_toolbar.js
|
|
|
|_views_
        |_about.tpl
        |_contact.tpl
        |_index.tpl
        |_listing.tpl
        |_post.tpl
        |_upload.tpl



************
#Routes: /
****
/          : GET : !
/<page:int>: GET : !

/pr/<id>/<product>: GET : 
/pr/<id>/<product>: POST : 


/login: GET : !
/login-validate: POST : !!

/register: GET : !!
/register-validate: POST : !!

/logout: GET : !


/account
/account/<page:int>

/cart: !
/add-cart/<id>
/del-cart/<id>

/upload: GET : 
/upload: POST :

/admin-track
/admin-track/<page:int>

/admin-track
/admin-track/<id:int>

/admin/update/validate/<id:int>

/gift-card/checkout
/gift-card/checkout/validate

/bac-validate
/bac/flutter/validate

/address/verify

/faq
/about-us
/delivery-info
/return-policy
/privacy-policy
/terms-of-use

/transaction/tracking/<id>

/forgot-password
/forgot-password-otp
/forgot-password-validate


************
#DATABASE: MySQL
****
bitstar
|__cart
|__comments
|__gift_card
|__product_listing
|__images
|__transaction_history
|__users

****
#CODE:
CREATE TABLE cart (
c_id INT AUTO_INCREMENT PRIMARY KEY,
u_id INT,
p_id INT,
topic TEXT,
features TEXT,
img TEXT,
qty TEXT,
price TEXT
);

CREATE TABLE comments (
c_id INT AUTO_INCREMENT PRIMARY KEY,
p_id INT,
author TEXT,
content TEXT,
hour TEXT,
minute TEXT,
month TEXT,
day TEXT,
year TEXT
);

CREATE TABLE gift_card (
id INT AUTO_INCREMENT PRIMARY KEY,
code TEXT,
pin TEXT,
hour TEXT,
minute TEXT,
day TEXT,
month TEXT,
year TEXT,
balance TEXT
);

CREATE TABLE product_listing (
id INT AUTO_INCREMENT PRIMARY KEY,
topic TEXT,
price TEXT,
brand TEXT,
file TEXT,
day TEXT,
month TEXT,
year TEXT,
features TEXT,
image TEXT
);

CREATE TABLE images (
p_id INT AUTO_INCREMENT PRIMARY KEY,
img_url TEXT
);

CREATE TABLE track (
id INT AUTO_INCREMENT PRIMARY KEY,
u_id INT,
minute TEXT,
hour TEXT,
day TEXT,
month TEXT,
year TEXT,
status TEXT,
payment TEXT,
total TEXT
);

CREATE TABLE transaction_history (
t_id INT AUTO_INCREMENT PRIMARY KEY,
g_id TEXT,
p_id TEXT,
u_id TEXT,

topic TEXT,
features TEXT,
quantity TEXT,
price TEXT,

address TEXT,
city TEXT,
zip TEXT,
state TEXT,

img TEXT,
minute TEXT,
hour TEXT,
day TEXT,
month TEXT,
year TEXT
);

CREATE TABLE users (
id INT AUTO_INCREMENT PRIMARY KEY,
first_name TEXT,
last_name TEXT,
email TEXT,
phone TEXT,
password TEXT,
hash TEXT,
otp TEXT,
status TEXT
);

CREATE TABLE banner (
p_id INT AUTO_INCREMENT PRIMARY KEY,
img_url TEXT
);