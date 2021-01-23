# MasterKlass

Hello there!

![GitHub last commit](https://img.shields.io/github/last-commit/thiagohardt/masterklass?style=for-the-badge) ![Languages](https://img.shields.io/github/languages/count/thiagohardt/masterklass?style=for-the-badge)


A live version can be found [here](https://masterklass.herokuapp.com/).

# UX

This project tries to create a Django application for a video subscription service.

The website is clean and intuitive, making navigation easy. 

## User Stories

 **As a Visitor**
 - As a Visitor, I want to easily understand the main purpose of the site.
 - As a Visitor, I want to be able to view courses available before buying a subscription.
 - As a Visitor, I want to be able to purchase a subscription.
  
 **As a User**
 - As a User, I want to easily understand the how to navigate through the site.
 - As a User, I want to be able to update and edit my profile.
 - As a User, I want to search all courses and lessons.
 - As a User, I want to comment on courses.

 **As a Staff Member**
 - As a Staff Member, I want to easily understand the how to navigate through the site.
 - As a Staff Member, I want to be able to update and edit my profile.
 - As a Staff Member, I want to search all courses and lessons.
 - As a Staff Member, I want to edit categories, courses and lessons.

## MVP

✅ Fully responsive.<br>
✅ Purchase a subscription. <br>
✅ Register a new account and login.<br>
✅ Edit profile. <br>
✅ Access online lessons. <br>
✅ Comments section. <br>
✅ User and Staff have different permissions. <br>
✅ Staff users can create and edit categories, courses and lessons. <br>


### Existing Features

- **New Account** <br>
To access the page the user must first create a new account by clicking on the "Signup" link on the navbar or button on landing page form. To vreate a new account you must buy a subscription.  

- **Login** <br>
To access the page the user must use his credentials to login. In the case of this build there is also an option to login as a "Demo User" or "Demo Staff" which allows the user experience the application utilizing a premade account. (refer to testing section) 

- **Profile** <br>
Shows your account information such as username, name, email and profile picture.

- **Edit Profile** <br>
Allows the user to close or edit account information such as name, email, password and profile picture.

- **Course Category** <br>
Courses are divided into different categories. 

- **Courses** <br>
Courses contain lessons. They also have a comment section where user can post messages.
They are organized in different categories. 

- **Lessons** <br>
Lessons are videos and are organized by courses. 


## Design
The whole UI is made utilizing Bootstrap 4.5. For further information, please refer to the official documentation [here](https://getbootstrap.com/docs/4.5/getting-started/introduction/).

### Wireframe
The wireframe for the project can be found [here](https://www.figma.com/file/wTAf7uOuDYff9SEiUaJf2q/MasterKlass-wireframe?node-id=102%3A5630).
During the project development lifecycle, more and more was added, making it a little more complex than what's showed in the wireframes.


### Typography

**Body:** Roboto<br>


## Technologies Used

Throughout the project, the following technologies were used.

- [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
- [CSS3](https://developer.mozilla.org/en-US/docs/Archive/CSS3)
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [jQuery](https://jquery.com/)
- [Bootstrap](https://getbootstrap.com/docs/4.5/getting-started/introduction/)
- [Stripe](https://stripe.com/en-ie)

	 
## Testing
Detailed tests can be found [here](https://github.com/ThiagoHardt/masterklass/blob/main/tests.md). 

## Test Accounts
For testing purposes these accounts can be used. Or feel free to create your own.

### Regular user
- Username: demo_user
- Password: demoaccount123

### Staff user
- Username: demo_staff
- Password: staffaccount123


## Deployment

The website is hosted and deployed by [Heroku](https://www.heroku.com/home).
Everything is deployed from the master branch and updates automatically whenever the branch is updated in GitHub.

1.  Log in Heroku (or create a new one if you don't have one.);
2.  Go to your dashboard.
3.  Click on the "New"  -> "Create new app" button located right under the navbar.
4.  Choose a unique name for your app.
5.  Choose a region (preferably close to where you are located).
6.  If everything works fine you should see the overview page of your app.
7.  Click on Settings tab.
8.  Reveal Config vars.
9.  Here we configure the SECRET_KEY, STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY, DATABASE_URL, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, EMAIL_HOST_USER, EMAIL_HOST_PASS, USE_AWS values (thoose are  not public and are the same values on my env.py file(which is also private)).
10. Click on deploy tab.
11. In the case of this project I chose to conect my app to my repository in GitHub, so it auto updates my heroku app whenever the project is pushed. 
12. Click on the Deploy Branch button. 
13. DONE!

### Forking
If you want to fork the repository to your own GitHub account you can by clicking on the “fork” button under the navbar with your profile.

### Cloning

 1. If you want to clone the repository into a local file you can by:
 2. Clicking on the green button “Code” and copying the url showed.
 3. Open GitBash
 4. Change directory to the desired location where you want to clone the
    files to.
 5. Type “git clone” and paste the copied URL
 6. Press enter and you should have your local file cloned and ready.
 7. After opening the folder you should create a new file in the root directory, name it env.py
 8. In env.py you can set your environment variables.  
    ```
      import os

        os.environ["SECRET_KEY"] = "<your_value>"
        os.environ["STRIPE_PUBLIC_KEY"] = "<your_value>"
        os.environ["STRIPE_SECRET_KEY"] = "<your_value>"
        os.environ["DATABASE_URL"] = "<your_value>"
        os.environ["AWS_ACCESS_KEY_ID"] = "<your_value>"
        os.environ["AWS_SECRET_ACCESS_KEY"] = "<your_value>"
        os.environ["EMAIL_HOST_USER"] = "<your_value>"
        os.environ["EMAIL_HOST_PASS"] = "<your_value>"
        # os.environ["DEVELOPMENT"] = "True" --> uncoment to use DEBUG MODE
        os.environ["USE_AWS"] = "True" --> set True or False to use AWS S3 Buckets

## Credits

### Content

- All content on the page was created by me. 
- This project was inspired by [Masterclass](https://masterclass.com/)

### Media

- All images used are from [Unsplash](https://unsplash.com/)
- All videos used are from [videvo](https://www.videvo.net/)

### Acknowledgements

-   My Mentor, **Oluwafemi Medale** for continuous helpful feedback.
