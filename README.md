# Boxing Gym

Milestone Project 4 - Full Stack Frameworks with Django

The website is created with the purpose to build an active community of boxing lovers.
The site will target the people who would like to start doing boxing and looking for a small but authentic boxing gym.
The business logic behind this website is to sell more subscription plans.
Existing members can easily change their subscription plan and buy boxing equipment in the site's Shop section. 

Go to website: https://boxing-gym-dp.herokuapp.com/

## UX

### Mockup
![Boxing gym mockup](/media/mockup.png)

### User stories

As a first time User I want:
-   To immediately understand what is the purpose of this website and easy navigate the site.
-	To read about the classes the gym offers
-	To see prices for fitness plans
-	To see timetable for classes
-	To read testimonials
-	To contact gym
-	To sign up for trial class
-	To see list of products

As a gym member I want:
-	To Log in and Log Out in my profile
-   To view individual product details
-	To view my previous purchases
-	To buy a fitness plan
-   To buy a products from webshop
-	Easily to recover my password in case I forget it

As a admin I want:
-	To add, edit and delete products in webshop

### Design Choices

The overall feel of the website is clean. 
Dark background and background images give the right feeling - boxing is a tough and very intense sport.

### Fonts

Font family for texts was choosen Lato.

### Colors

The website's background color was chosen black with the light texts and light elements on it.
As CTA element color was chosen red to create the contrast on the page.

### Icons

Icons were chosen to use as a design element on the landing page. The icon color is red, to stand out on the page.

Website consists of 11 sections:

- **Landing page**
- **Join Us**
- **Free Trial**
- **Classes**
- **Shop**
- **Product page**
- **Shopping bag**
- **Checkout**
- **Contact** 
- **User profile page**

Wireframes are available here:

![Landing page](/media/wireframes/landing.png)
![Landing page mob](/media/wireframes/landing-mob.png)
![Fitness plans](/media/wireframes/plans-tab.png)
![Fitness plans](/media/wireframes/plans.png)
![Trial session](/media/wireframes/trial.png)
![Shop](/media/wireframes/Shop.png)
![Shopping bag](/media/wireframes/shopping-bag1.png)
![Shopping bag](/media/wireframes/checkout-mob.png)


## Features

### Existing Features

Navbar on top helps users easy to navigate through the website. Web site's Name in the left corner always brings the user back to the Landing page. On the medium and small sizes, the user can open the navbar from the burger icon on the right top of the website. Section My Account gives user the option to Register or Log In. Only registered users can buy fitness plans or equipment from an online Shop.

### Landing page

The Landing page consists of several parts. The hero section consists of the background image and two CTA buttons. Hero image gives a clear understanding of what is this website about. Further down, there is a training section, where user can see the training this gym offers. Read more link takes the user to the Classes section where is possible to read more details about these training. The Gym facilities section with 6 high-quality images introduces user to the Boxing gym environment. Testimonials and short Boxing gym description follow further down the landing page.

### Join Us

As a user, you are able to read and choose from 3 fitness plans this Boxing gym offers. By clicking CTA Choose Plan user is asked to sign in or sign up for this page. After logging in, the user can pay for a chosen fitness plan, by filling asked credit card details.

### Classes

As a user, you can read more detailed about the boxing classes and times by clicking Classes on the Navigation bar.

### Shop

As a user, you can see boxing equipment in the website's Shop section. You need to be registered to make a purchase. Once the user press on the product, Sign in form appears. After signing in, the product detail section opens, where user can read more detailed about the product, choose quantity and add the product to the shopping bag, or keep shopping by choosing one of the CTA options. 
Once the user is taken to the Shopping bag section there are options to update the quantity or remove the product from the bag. As a user, you can see the product image, info, and total price. Two CTA options take the user back to the Shop section or Secure checkout where the user is asked to fill in credit card details to finish the purchase.

### Contact

As a user, you can see contact details in the Contact section of the website.

### My Account

As a first-time user, under the section My account you have two options - Register or Login. As a registered user, you have an option My profile, where user can see one's previous purchases if there is any or Logout from the profile.

### Product Management

As an admin, you are able to manage existing products in the webshop.
If you are logged in with an admin username, your Navbar shows the option Product Management. Pressing the link, an admin has been directed to the product page, where all products are listed in columns and offers the option Edit or Delete them. As an admin, you are able to Add, Edit, or Delete the Product by pressing the CTA buttons. Pressing the button Add new product admin can see a form that needs to be filled in and submitted. After submitting admin has been directed back to the product page where the added product has been listed together with others.

### Features left to implement

- In the future, I would like to add a booking system to this website, where gym members can book their time for classes.
- I would like to implement that members can see on their Profile page what fitness plan they have and when is the next automatic payment for it. Also the option to replace existing fitness plans with the new one.

## Technologies Used

- HTML
- CSS 
- JavaScript
- Python+Django
- [Bootstrap v5.1](https://getbootstrap.com/docs/5.1/getting-started/introduction/)
- jQuery
- Stripe 
- MySQL

## References

- Code institute video projects, especially Boutique Ado
- [W3schools](https://www.w3schools.com/)
- [Stackoverflow](https://stackoverflow.com/) 

## Testing

For testing code validity i used:

* [HTML Validator](https://validator.w3.org/)
* [CSS Validator](https://jigsaw.w3.org/css-validator/)
* [JavaScript Validator](https://jshint.com/)
* [Python Validator](http://pep8online.com/)

### User stories testing

1. As a first time visitor, I want to immediately understand what is the purpose of this website and easy navigate the site.
    * Hero image, logo and headline gives clear indications about purpose of the site.
    * Navigation bar is easy to find and use.
    * The logo on the left corner always leads back to home page.

2. As a first time visitor, I want to read about the classes the gym offers.
    * On the home page, there is a section calls Our Group Training, Read more links under each training's description takes to the section Classes & Time table, where all information about the classes is listed.
    * On the navigation bar there is section name Classes, which takes directly to the section, where all information about the classes is listed.

3. As a first time visitor, I want to see prices for fitness plans.
    * CTA button Join Now on hero image takes to the section with all fitness plan offers.
    * On the navigation bar, section Join Us takes to the section with all fitness plan offers.

4. As a first time visitor, I want to see timetable for classes.
    * On the home page, there is a section calls Our Group Training, Read more links under each training's description takes to the section Classes & Time table, where is the timetable for all classes.
    * On the navigation bar there is section Classes, which takes directly to the section, where is the timetable for all classes.

5. As a first time visitor, I want to read testimonials.
    * On the home page, there is a section What Our Members Say with testimonials from existing gym members.

6. As a first time visitor, I want to contact gym.
    * On the navigation bar, there is a section Contact, which takes to the gym contact page.

7. As a first time visitor, I want to sign up for trial class.
    * CTA button Sign Up For Free Trial on hero image takes to Sign Up form.
    * Filling the form and clicking Send, flashes the message "YOUR REQUEST HAS BEEN SUBMITTED" and the confirmation email has been received.
    * The form can be submitted only after checking the Terms and Conditions agreement box under the form.
    * Correct type of email should be entered.

8. As a first time visitor, I want to see list of products.
    * On the navigation bar, there is a section Shop where all available products are shown.

10. As a gym member, I want to Log in and Log Out in my profile.
    * Sign In link is easy to find on the navigation bar under the section My Account.
    * Entering wrong Username/Password flashes message "The username and/or password you specified are not correct."
    * Once the form is submitted opens the home page.
    * Sign Out link is easy to find on the navigation bar under the section My Account.
    * After clicking the Sign Out link confirmation question and button opens, which needs to be clicked before being signed out.

11. As a gym member, I want to view individual product details.
    * Only registered users can view individual product details.
    * Once signed in, clicking on the individual product, opens the product page with product image, description, option to choose the quantity, and Add To Bag CTA.

12. As a gym member, I want To view my previous purchases.
    * On the navigation bar, under the My Account section clicking My Profile, opens the page with all previous purchases if there is one.  

13. As a gym member, I want to buy a fitness plan.
    * Only registered users can buy a fitness plan.
    * Non-registered are asked to Sign In or Sign Up before the purchase.
    * On the home page, CTA Join Now opens the fitness plan section where offered plans are listed. 
    * Clicking Choose Plan opens the payment form which needs to be filled in before finishing the payment.
    * Payment can be finished by clicking CTA button Pay and Subscribe.
    * At the end of the process, flashes confirmation message, "Thank You for Subscribing" 
    * If the information in the form has been filled wrong, flashes error message 500 - Internal Server Error and CTA Go To Homepage, which takes back to home page.

14. As a gym member, I want to buy a products from webshop.
    * Only registered users can buy products from the webshop.
    * Non-registered are asked to Sign In or Sign Up before the purchase.
    * When a chosen product is added to the bag, Shopping Bag page opens.
    * It is possible to change the quantity of the product or delete the product from the bag and return to the shopping page.
    * To confirm the purchase is possible by clicking CTA Secure Checkout, which takes to card detail form.
    * The total amount is still visible above the form.
    * The card detail form needs to be filled with payment card information and approved by clicking CTA Pay, which finishes the purchase.
    * After clicking the confirmation button, flashes message "Thank You For Purchasing!".
    * If the information in the form has been filled wrong, flashes error message 500 - Internal Server Error and CTA Go To Homepage, which takes back to home page.

15. As a gym member, I want easily to recover my password in case I forget it.
    * Under Sign In form, there is the link Forgot Password?, which takes to the Password Reset page.
    * Entering email address and clicking CTA Reset My Password, flashes confirmation message, that the email with link has been sent.
    * After receiving the email and clicking the password reset link, opens a page with the option to change the password.
    * By typing a new password two times and confirming it, the password has been changed. Flashes message "Your password is now changed".

16. As a admin, I want to add, edit and delete products in webshop.
    * Once admin is logged in Product management link is easy to find in the navigation bar under the section My Account.
    * Product management page consists of all webshop products and Add, Edit, and Delete CTA.
    * Clicking the Add new product button opens a form which admin needs to fill in and submit the form by clicking Add Product button.
    * The new product has been added to the webshop with other products on the Shop page.
    * Clicking the Edit button opens a form with an existing Product.
    * Admin can change the information and Update the form or Cancel the action by clicking the Cancel button.
    * Clicking the Delete button the product has been deleted.

## Deployment

The website is hosted usign GitHub and deployed to Heroku.
I started by creating a new repository with `git init`. Then each update was done by the command `git add -A` and then committing it to my local repo with the command `git commit -m ”message”`.
Then I uploaded it to my remote repo (Github) using `git push`.

To deploy website to Heroku, I take following steps:
- Create a requirements.txt file by writing terminal command pip freeze --local > requirements.txt.
- Create Procfile using terminal command echo web: python app.py > Procfile.
- Log In into my Heroku.com account and click "New" > "Create New App" button in my dashboard. Give it a name and set the region to Europe.
- From the dashboard, click "Deploy" and choose GitHub as Deployment method. That will setup automatic deployment from GitHub repository.
- Add my repository name and confirm it by clicking "Connect".
- From the dashboard, click "Settings" > "Reveal Config Vars".
- Back in terminal write command git add requirements.txt and git commit -m "Add requirements.txt", 
the same with Procfile - git add Procfile and git commit -m "Add Procfile" and then git push the project to GitHub.
- In the heroku dashboard click "Deploy". 

## Credits

## Content

All the content on this website was written, inspired by several boxing-related websites and forums all over the world.

### Media

Images for this site were taken from [Unsplash](https://unsplash.com/).
Product images were taken from [Google](https://google.com/).

### Acknowledgements

- I received inspiration for this project from Code Institute Boutique Ado project
- Slack community
- My mentor Spencer Barriball

Website is created for educational use!