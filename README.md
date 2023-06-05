# STEM & LEAF - A PLANT CARE SPACE FOR BEGINNERS

## Author
Cara McAvinchey 

## Project Overview
*  The Stem & Leaf blog is a place for plant care beginners to visit and learn about how to take care of their plants. Each blog post is dedicated to a popular house plant, with a short write up and care tips. 
* You can view the deployed website [here](https://stem-and-leaf-blog.herokuapp.com/).

<img width="700" alt="image" src="https://user-images.githubusercontent.com/97494262/209436822-8a40360c-cb65-4abf-bd98-5869aec18d12.png">

## TABLE OF CONTENTS
- [STEM & LEAF - A PLANT CARE SPACE FOR BEGINNERS](#stem---leaf---a-plant-care-space-for-beginners)
  * [Author](#author)
  * [Project Overview](#project-overview)
  * [UX](#ux)
    + [Project Goal](#project-goal)
    + [User Stories](#user-stories)
  * [DESIGN CHOICES](#design-choices)
    + [Colors](#colors)
    + [Typography](#typography)
    + [Images/Icons](#images-icons)
    + [Animations](#animations)
    + [Responsiveness](#responsiveness)
  * [WIREFRAMES](#wireframes)
    + [Post List](#post-list)
    + [Post Detail](#post-detail)
  * [FEATURES/STRUCTURE](#features-structure)
    + [Navigation](#navigation)
    + [Plant List](#plant-list)
    + [Plant Detail](#plant-detail)
    + [Likes](#likes)
    + [Comments](#comments)
    + [Register](#register)
    + [Login/Logout](#login-logout)
    + [Footer](#footer)
    + [Error 404/403/500](#error-404-403-500)
    + [Features for Future Development](#features-for-future-development)
  * [DATA MODEL](#data-model)
  * [TESTING](#testing)
    + [Validation Testing](#validation-testing)
    + [Cross Browser and Cross Device Testing](#cross-browser-and-cross-device-testing)
    + [Manual Testing](#manual-testing)
    + [Automatic Testing](#automatic-testing)
    + [Outstanding Defects](#outstanding-defects)
    + [Defects of Note](#defects-of-note)
  * [ACCESSIBILITY](#accessibility)
    + [Lighthouse Audit](#lighthouse-audit)
    + [Keyboard Navigation](#keyboard-navigation)
  * [TECHNOLOGIES USED](#technologies-used)
  * [DEPLOYMENT](#deployment)
  * [CREDITS](#credits)
    + [Media](#media)
  * [ACKNOWLEDGEMENTS](#acknowledgements)

## UX

### Project Goal
* The aim of the project is to provide easily digestible information about popular house plants for beginners and to allow for conversation and sharing of experiences in taking care of them.

### User Stories
* For sight users:
1. As a **site user**, I can **register an account** so that **I can interact with blog posts**.
2. As a **site user**, I can **view a list of posts** so that **I can select one to read**.
3. As a **site user**, I can **click on a post** so that **I can read the full article** and find out more about plant care.
4. As a **site user**, I can **view the number of likes on each post** so that **I can see which plants are popular.**
5. As a **site user**, I can **like a post** so that **I can engage with the blog content**.
6. As a **site user**, I can **view comments on a post** so that **I can read other user feedback**.
7. As a **site user**, I can **leave comments on a post** so that **I can share my own feedback.**
8. As a **site user**, I can **edit and delete my comments on a post** so that **I can customise or remove my thoughts** if required.
9. As a **site user**, I can **use the search bar** so that **I can find plants I am looking for**.
10. As a **site user**, I can **save my favourite plant posts** so that **I have all my houseplants I care for in the same place.**
11. As a **site user**, I can **rate blog posts on a scale of 1-5** so that **I can give feedback about which content I enjoy most**.
12. As a **site user**, I can **return to the home page** of the blog if there is an error so that **I don’t get lost on the website**.

* For admin users:
13. In order to **create and control the content for the blog** as an **admin user**, **I can access the admin panel using admin login details.**
14. In order to **finish writing or publish content later** as an **admin user**, **I can create draft posts.**
15. In order to **manage the blog content** as an **admin user**, **I can create, read, update and delete posts** using the admin panel.
16. In order to **maintain a positive community atmosphere** as an **admin user**, **I can approve/disapprove comments.**  
 
## DESIGN CHOICES

### Colors
<img width="538" alt="image" src="https://user-images.githubusercontent.com/97494262/209437405-63db90ed-fd86-4285-8a19-002c73a2d1a7.png">
 
- The natural color palette links to the theme of plants and plant care. 
- The headings, icons and body text are darker to ensure clear contrast and readability for the user across the site.
- The green header and footer ensures clear contrast and delineation between sections.
- Due to the lighthouse score for accessibility, the background color for the header and footer was adjusted:

<img width="400" alt="image" src="https://user-images.githubusercontent.com/97494262/210070268-17725578-409a-4278-a99e-60e844ddb1b8.png">

### Typography
<img width="500" alt="image" src="https://user-images.githubusercontent.com/97494262/209437426-7c754f60-85b0-4d60-9f17-04caedb8f635.png">

- The font combination was chosen using guidance article from Mai Knoblovits [here](https://artisanthemes.io/great-google-font-combinations-ready-use/).
- The logo and headings use Amatic SC with a fallback of cursive and the body text uses Roboto Condensed with a fallback of san-serif.
- The choice of fonts were selected and installed using [Google Fonts](https://fonts.google.com/).

### Images/Icons
<img width="351" alt="image" src="https://user-images.githubusercontent.com/97494262/209437645-30a1ff77-27cb-4eea-a342-6aa1592cb81d.png">

- The icons were chosen to provide clear understanding of each plant and its care requirements.
- Each summary card has the same information structure with all icons standard throughout the site.

### Animations
- The navbar, social icons and buttons across the site have a subtle grow effect when hovered over by the user.
- All links have a color change and underlined effect when hovered for clear distinction from the body text.

### Responsiveness
- The website was designed mobile-first using flexbox to ensure responsiveness throughout the website.
- The standard grid from Bootstrap was used to achieve this.

## WIREFRAMES

### Post List
- The post list page was designed using cards to show a quick summary of each plant.
- The user can click and find out more about a plant that interests them.
<img width="636" alt="image" src="https://user-images.githubusercontent.com/97494262/209437372-83b2bc1e-68a0-4a75-8e86-d78b69df4a7d.png">

### Post Detail
- Each blog post provides detail about the plant and a list of instructions to care for it. 
- The registered user can also comment and like the post if desired.
<img width="611" alt="image" src="https://user-images.githubusercontent.com/97494262/209437385-b8be9fe9-bbbb-4110-a9af-e0f5239f3cc9.png">

## FEATURES/STRUCTURE

### Navigation
- The users will have a choice of home, login/logout & register when visiting the site. 
- There is a subtle hover state on each of the navigation items for better user experience.
- For mobile devices, the navigation toggles to a hamburger menu.

### Plant List
- The users will have a list of posts with a title, excerpt and summary card of care required for each plant.
- The image and title are linked, so users may click on either and be taken to the plant detail page.
- There is a hover state on the title to show the user they can click on the post.
- This summary card is later repeated in each plant detail post for continuity across the site.

<img width="276" alt="image" src="https://user-images.githubusercontent.com/97494262/210070669-031252b8-33af-4c74-9efe-17c2b4278235.png">
<img width="500" alt="image" src="https://user-images.githubusercontent.com/97494262/210070722-3dea018c-60c0-4793-847e-d4f9f2cacbdb.png">

### Plant Detail
- Each post has a short article about the plant including its care information in detail.
- The structure of each post is consistent, starting with the card at the top and excerpt from the plant list and then the main content and bulleted list of care instructions at the end. 

<img width="600" alt="image" src="https://user-images.githubusercontent.com/97494262/210071425-5ef9d25e-45f6-4c66-8373-e594f0048770.png">

<img width="500" alt="image" src="https://user-images.githubusercontent.com/97494262/210071401-56dd2bb4-83d0-4587-931a-3ef062a84776.png">

### Likes
- If the user isn't logged in, they will see the below information:

<img width="673" alt="image" src="https://user-images.githubusercontent.com/97494262/210071488-dcd28c40-fe6c-418f-92f9-090d2cba1465.png">

- If the user is logged in, they will be able to like the post:

<img width="284" alt="image" src="https://user-images.githubusercontent.com/97494262/210071552-630d2e30-1c78-458f-83d8-4b8122a6c7c0.png">

- The user is able to easily return to the home page using the go back button or clicking the logo at the top of the page.

### Comments
- If a post doesn't have any comments, the user will see the below if not logged in:

<img width="481" alt="image" src="https://user-images.githubusercontent.com/97494262/210071767-5a59d9be-2797-4f93-8de8-e647fa16103e.png">

- If logged in, users will be encouraged to share their experience in caring for the plant they've read about:

<img width="500" alt="image" src="https://user-images.githubusercontent.com/97494262/210071679-732036f7-0a99-4d22-a807-b822c2545ce7.png"> 

- The user will be able to edit their comment using a form and be alerted using a message that disappears after 3 seconds.

<img width="500" alt="image" src="https://user-images.githubusercontent.com/97494262/210083125-faa24f47-ec2b-432f-ac90-105375a49f08.png">

<img width="500" alt="image" src="https://user-images.githubusercontent.com/97494262/210083087-7ff6c85b-1770-4f47-b723-d03d993b955f.png">

- The user will be able to delete their comment after being prompted and can go back if desired or will proceed and receive a success message:

<img width="486" alt="Screenshot 2022-12-30 at 14 19 16" src="https://user-images.githubusercontent.com/97494262/210080212-009dfbe4-787d-448f-b498-97e3add086ae.png">

<img width="500" alt="image" src="https://user-images.githubusercontent.com/97494262/210080130-61cd8839-a2b1-4b88-a7cf-227fe27beb57.png">

### Register 
- The user will be able to easily sign up as a user using the below form.
- If users are already registered, there is a link to easily navigate to login instead

<img width="701" alt="image" src="https://user-images.githubusercontent.com/97494262/210072154-73833448-d460-49f4-958f-5ba1ebd5dae8.png">

### Login/Logout 
- The users can easily sign in using the below form with an option to 'remember me' if desired.
- If a user hasn't registered, there is a link to easily navigate to sign up instead.

<img width="574" alt="image" src="https://user-images.githubusercontent.com/97494262/210072279-5f61cc40-a083-4994-905d-8edbfc3da545.png">

- The user is prompted with a message before logging out:

<img width="439" alt="image" src="https://user-images.githubusercontent.com/97494262/210072389-f62bc7ca-1877-4ec5-8ff3-a7a14f74f583.png">

- The user will receive a message that disappears after 3 seconds to say they have logged in/logged out:

<img width="694" alt="image" src="https://user-images.githubusercontent.com/97494262/210072803-acb43896-c62a-4e41-803f-0aefaf0cc50c.png">

<img width="704" alt="image" src="https://user-images.githubusercontent.com/97494262/210072771-813c77b7-c54c-4d51-b8ef-55683a9a3d2e.png">

### Footer
- The footer links directly to the social media pages of the plant care blog.
- There is a subtle hover state on each icon for better user experience.

### Error 404/403/500
- There are error pages in place in case a user is taken to a restricted area or the page doesn't exist.
- The return home button will take the user back to the plant list page.

<img width="460" alt="image" src="https://user-images.githubusercontent.com/97494262/210073145-f3d43565-d722-4a8f-866c-2ed0e1fc50ec.png">
<img width="613" alt="image" src="https://user-images.githubusercontent.com/97494262/210073167-f80d0d34-41c5-4fb9-a8ac-53da96d3631f.png">
<img width="538" alt="image" src="https://user-images.githubusercontent.com/97494262/210073183-e8f315ba-264c-47cc-a540-e16677fe583d.png">

### Features for Future Development
- It will become less efficient for the user to scroll through many posts in the list view so a search bar will allow users to find specific plants they want to read more about.
- It would increase user experience to add a method to 'save' blog posts so users can keep their favourite plants in one place.
- To increase user interactivity from readers, users could rate blog posts on how helpful the information was and give feedback.
- Pending comments can be added so users are aware they are awaiting approval. 

## DATA MODEL
<img width="484" alt="image" src="https://user-images.githubusercontent.com/97494262/209538748-6f3cdc41-16c5-43ab-94a8-2341239ffc78.png">

- [X] C - Site users can create/register their own profile to interact with the plant posts.
- [X] R - Site users can open and read the plant blog posts and read comments from other users.
- [X] U - Site users can like a post, updating the details and analytics for a plant detail post.
- [X] D - Site users can eliminate their like if desired on a plant detail post.

<img width="477" alt="image" src="https://user-images.githubusercontent.com/97494262/209538824-f613791d-53b6-43e4-a305-f14a52026443.png">

- [X] C - Site users can create their own comments using a form on each blog post.
- [X] R - Site users can read comments from other users.
- [X] U - Site users are able to update/edit their comments using a form.
- [X] D - Site users are able to delete their comments.

## TESTING

### Validation Testing
- HTML
   - No errors were returned when passing through the official [HTML validator]("https://validator.w3.org/nu/?doc=https%3A%2F%2Fcaramcavinchey.github.io%2Frock-paper-scissors%2F").

**Post List**
<img width="500" alt="image" src="https://user-images.githubusercontent.com/97494262/210156718-b0e52c29-0edf-46b7-9e13-eed62b1bb787.png">
   
**Post Detail**
<img width="500" alt="image" src="https://user-images.githubusercontent.com/97494262/210156567-eb2b02a0-596a-4a52-ade9-213ee00dfbae.png">

**Sign up**
<img width="500" alt="image" src="https://user-images.githubusercontent.com/97494262/210156724-f2aab13c-453a-4556-9a5a-af64cff6f888.png">

**Sign in**
<img width="500" alt="image" src="https://user-images.githubusercontent.com/97494262/210156731-bf8dfff2-c326-4ebb-a826-905e213f9536.png">

**Edit Comment**
<img width="500" alt="image" src="https://user-images.githubusercontent.com/97494262/210156740-9699a4c3-1671-489f-b869-760ba3de554f.png">

- CSS
   - No errors were found when passing through the [CSS validator]("https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fcaramcavinchey.github.io%2Frock-paper-scissors%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en").

<img width="500" alt="image" src="https://user-images.githubusercontent.com/97494262/210075568-6efc11bf-8f09-4ec8-8eae-c3936a1678df.png">

- JavaScript
   - No errors were found when passing through the [JS validator]("https://jshint.com/").
   
<img width="500" alt="image" src="https://user-images.githubusercontent.com/97494262/210155726-28197ad7-5f34-49d1-bc1c-5991f2b29533.png">

### Cross Browser and Cross Device Testing
- The below combination of devices, browsers, and operating system were used to test the website. A range of viewport sizes were checked to see if users would have the same experience across multiple devices and browsers.

| **TOOL / Device**           | **BROWSER**      | **OS**  | **SCREEN WIDTH** |
|-----------------------------|------------------|---------|------------------|
| dev tools: Galaxy Fold      | Chrome           | android | 280 x 653 px     |
| dev tools: iPhone SE        | safari           | iOs     | 375 x 667 px     |
| dev tools: Pixel 2          | Chrome           | android | 411 x 731        |
| real phone: iPhone XR       | safari           | iOs     | 414 x 896 px     |
| browserstack: Nexus 7       | Firefox          | android | 960 x 600 px     |
| browserstack: iPhone 13 Pro | safari           | iOs     | 390px × 844px    |
| real tablet: iPad Pro 11    | Chrome           | iOs     | 834 x 1075 px    |
| real laptop: Macbook Pro    | Firefox & Chrome | iOs     | 1400 x 766 px    |
| broswerstack                | Firefox          | iOs     | 1440 x 672 px    |
| browserstack                | Edge 99          | windows | 1440 x 672 px    |

### Manual Testing
- You can view manual testing of the website [here](https://docs.google.com/spreadsheets/d/123Pia98Ms_Fe6at0hPnAWhcNrmeVc4X2RLYmD7VsqX4/edit?usp=sharing).

### Automatic Testing
- Manual testing was done due to time constraints.

### Outstanding Defects
- There are no outstanding defects.

### Defects of Note
- The user story for [OPEN A POST](https://github.com/CaraMcAvinchey/stem-and-leaf-blog/issues/8) had multiple challenges including styling issues with the summary card, the likes/comments area and rendering of the plant detail model information. 
 - The styling challenges were solved using margins and restructuring of some div elements.
 - The comments/likes area required some guidance from my mentor to establish what the user sees when logged in, logged out and restructured the template from there.

## ACCESSIBILITY

### Lighthouse Audit
- The deployed website was run through lighthouse to check performance, accessibility, best practices and SEO scores.

<img width="650" alt="image" src="https://user-images.githubusercontent.com/97494262/210155754-2d11ca71-a553-47a9-a94b-41fd4c1aebd9.png">

### Keyboard Navigation
- The users will be able to use the tab button to navigate the website if required.

## TECHNOLOGIES USED
- GitPod
- GitHub
- Django
- Bootstrap
- Cloudinary
- Summernote
- Crispy Forms
- Heroku
- Balsamiq
- Fontawesome

## DEPLOYMENT

### ElephantSQL
1. Login to ElephantSQL, access the dashboard and create a new instance (input a name, choose tiny turtle, select a region).
2. Return to the dashcoard, copy the URL.

### Heroku
1. Create a new app in Heroku, choose a unique name and region.
2. Go to settings and add a new config var of ``` DATABASE_URL ```python with the value of the URL from ElephantSQL.
3. Add host name of the Heroku app name to ALLOWED HOSTS in settings.py:

```python
ALLOWED_HOSTS = ['{heroku deployed site URL here}', 'localhost' ]
```
### GitHub/GitPod
1. Create a new repository on GitHub, open a new workspace with GitPod.
2. Install django ```pip3 install 'django<4```python to install Django 3.2 the LTS (Long Term Support) version.
3. Create a new project and run the server to see if the app has installed.
4. Run migrations, create a super-user with a username, email and password. 
5. Install ```  pip3 install dj_database_url==0.5.0 psycopg2 ``` and freeze requirements ``` pip freeze > requirements.txt```
6. Add ``` import os``` and ```import dj_database_url``` to settings.py
7. Connect the new database, paste in the ElephantSQL URL (do not commit at this stage):
 
```python
 # DATABASES = {
 #     'default': {
 #         'ENGINE': 'django.db.backends.sqlite3',
 #         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
 #     }
 # }
 
 DATABASES = {
     'default': dj_database_url.parse('your-database-url-here')
 }
```
8. Ensure connection to the external database, run ```python3 manage.py showmigrations``` then run ```python3 manage.py migrate```
 <img width="740" alt="image" src="https://github.com/CaraMcAvinchey/stem-and-leaf-blog/assets/97494262/4d3f4186-3d58-4cff-8f27-8fc8c77edf58">
9. Create a new superuser for the new database, same as above.
10. Create an if else statement to setup development and external databases:

 ```python
 if 'DATABASE_URL' in os.environ:
    DATABASES = {
      'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
      }
    }
 ```
11. Install ```pip3 install gunicorn``` and run ``` pip freeze > requirements.txt```
12. Create a Procfile in the root directory and include ```web: gunicorn project_name.wsgi:applications```
13. Generate a SECRET_KEY, add it to Heroku config vars.
14. Create env.py file (ensure it is included in .gitignore file) and add the SECRET_KEY & DATABASE_URL to environment variables:
<img width="372" alt="image" src="https://user-images.githubusercontent.com/97494262/209531222-599282ee-2c54-490f-b543-1f09e5255490.png">
15. Edit settings.py to the below:
```python
SECRET_KEY = os.environ.get('SECRET_KEY', ' ')
```
```python
DEBUG = 'DEVELOPMENT' in os.environ
```
![image](https://github.com/CaraMcAvinchey/purrfect-sitters/assets/97494262/ceb9f1d4-35e8-47cd-ba04-6cd07bd8fe37)

<img width="301" alt="image" src="https://user-images.githubusercontent.com/97494262/209532128-acaa1e29-edea-45c3-93ce-2caaf0f71862.png">

19. Add, commit and push to GitHub.
20. Go to Heroku, add ```DISABLE_COLLECT_STATIC = 1``` to Heroku config vars.
23. Connect the project to the GitHub repository using personal account login.

24. Login to Cloudinary, copy the API Environmental variable to dashboard and add to env.py (see screenshot above) & to Heroku config vars:

<img width="571" alt="image" src="https://user-images.githubusercontent.com/97494262/209533286-4a79143c-6568-4055-99fc-76dd5821a02b.png">

27. Add cloudinary to installed apps in settings.py, add static/media file settings:

<img width="407" alt="image" src="https://user-images.githubusercontent.com/97494262/209533445-8f6670c5-490b-4294-95cf-febaaaed2ab2.png">

<img width="500" alt="image" src="https://user-images.githubusercontent.com/97494262/209533629-ab3fb31b-f096-4305-996e-970e4c950a3f.png">

28. Add template directories in settings.py, add Heroku host name to allowed hosts and add directory files:

<img width="600" alt="image" src="https://user-images.githubusercontent.com/97494262/209533879-b8284837-e7a1-4315-83e6-9b88d2125882.png">

<img width="501" alt="image" src="https://user-images.githubusercontent.com/97494262/209534100-46723f98-7bd6-40ed-91c1-5226ad6e950d.png">

<img width="313" alt="image" src="https://user-images.githubusercontent.com/97494262/209534271-772afed4-f299-45dc-b72d-d0843b7ad189.png">

25. Go to settings in Heroku and perform a manual deployment and check for any issues.
36. Go to Heroku settings, enable automatic deployments.

## CREDITS
- The Code Institute 'I Think, Therefore I Blog' walkthrough project assisted and guided in the setup and basic structure of this project.
- The Stockbook Project by Massimo Ranalli assisted with the setup of the edit/delete functions for comments as well as the messaging alerts.
- Code Institute Student Template: [gitpod full template](https://github.com/Code-Institute-Org/gitpod-full-template).
- The articles on the blog were written myself and any additional helpful articles were linked to for the user to access for more information.

### Media
- The fonts were chosen with guidance from an article written by Mai Knoblovits [here](https://artisanthemes.io/great-google-font-combinations-ready-use/).
- The colors for the website was generated using [Color Space]([https://coolors.co/image-picker](https://mycolor.space/?hex=%2333C883&sub=1)).
- The plant images were sourced using [Pexels](https://www.pexels.com) and [Pixabay](https://pixabay.com/).
- The icons for the favicon, footer, about page and location headings were taken from [Font Awesome](https://fontawesome.com/).
- The favicon image was converted using [Favicon.io](https://favicon.io/).

## ACKNOWLEDGEMENTS
- Thank you to my mentor for continuous helpful feedback and support throughout the project.
- The tutors at Code Institute for their patience and support.
- The Code Institute Slack community for tips and guidance.

[Back to the beginning](#table-of-contents)
