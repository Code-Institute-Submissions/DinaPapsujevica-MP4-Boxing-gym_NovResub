# Boxing Gym

Milestone Project 4 - Full Stack Frameworks with Django

The website is created with the purpose to build an active community of boxing lovers.
The site will target the people who would like to start doing boxing and looking for a small but authentic boxing gym.
The business logic behind this website is to sell more subscription plans.
Existing members can easily change their subscription plan and buy boxing equipment in the site's Shop section. 

Go to website: 

## UX

### Mockup
![Boxing gym mockup]()

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
-	To change my fitness plan
-	Easily to recover my password in case I forget it
-	Easily select quantity of a product when purchasing it

As a site owner I want:
-	To manage all member data
-	To add and delete products and fitness plans

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
![Trial session](/media/wireframes/trial.png)
![Shop](/media/wireframes/Shop.png)
![Shopping bag](/media/wireframes/shopping-bag.png)
![Shopping bag](/media/wireframes/shopping-bag.png)

## Features

### Existing Features

### Features left to implement

## Technologies Used

- HTML
- CSS 
- JavaScript
- Python+Django
- [Bootstrap v5.1](https://getbootstrap.com/docs/5.1/getting-started/introduction/)
- jQuery
- Stripe 
- database??


## References

## Testing

For testing code validity i used:

* [HTML Validator](https://validator.w3.org/)
* [CSS Validator](https://jigsaw.w3.org/css-validator/)
* [JavaScript Validator](https://jshint.com/)
* [Python Validator](http://pep8online.com/)

### User stories testing

1. As a first time visitor, I want to immediately understand what is the purpose of this website and easy navigate the site.
2. As a first time visitor, I want to read about the classes the gym offers.
3. As a first time visitor, I want to see prices for fitness plans.
4. As a first time visitor, I want to see timetable for classes.
5. As a first time visitor, I want to read testimonials.
6. As a first time visitor, I want to contact gym.
7. As a first time visitor, I want to sign up for trial class.
8. As a first time visitor, I want to see list of products.
9. As a first time visitor, I want to view individual product details.
10. As a gym member, I want to Log in and Log Out in my profile.
11. As a gym member, I want to view my subscription and purchases.
11. As a gym member, I want to change my fitness plan.
12. As a gym member, I want easily to recover my password in case I forget it.
13. As a gym member, I want easily select the size and quantity of a product when purchasing it.
14. As a site owner, I want to manage all member data.
15. As a site owner, I want to add and delete products and fitness plans.

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

KEY | VALUE
----|-----
IP | 0.0.0.0
PORT | 5000
SECRET_KEY | <your_secret_key>
MONGO_URI | mongodb+srv://<username>:<password>@<cluster_name>.6wwxi.mongodb.net/<database_name>?retryWrites=true&w=majority
MONGO_DBNAME | <database_name>

- Back in terminal write command git add requirements.txt and git commit -m "Add requirements.txt", 
the same with Procfile - git add Procfile and git commit -m "Add Procfile" and then git push the project to GitHub.
- In the heroku dashboard click "Deploy". 

## Credits

## Content

### Media

All images for this site was taken from [Unsplash](https://unsplash.com/).

### Acknowledgements

Website is created for educational use!