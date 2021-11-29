# The Drunken Goblin (Milestone Project 3)

![The Drunken Goblin](/static/images/responsive.jpg)

[Visit My Site Here](https://the-drunken-goblin.herokuapp.com/)

## Overview
The Drunken Goblin is a site that provides users with a database to find, create, edit and share role playing characters. It allows users to log in, view
their own characters, edit and remove them, and also contains a place where all characters stored into the database can be seen.

## Table of Contents

[UX](#ux)

[Features](#features)

[Technologies Used](#technologies)

[Testing](#testing)

[Deployment](#deployment)

[Credits](#credits)

<a name="UX"></a>

## UX
### User Stories
#### A First Time Visitor
- I want to be able to navigate the site easily and understand what it is for.
- I want to be able to look for role-playing characters that suit my needs.
- I want to navigate the site easily, know what page I'm on, and be able to use the site to obtain all the information I need.
- I want to be able to create an account and create my own characters.

#### A Returning User
- I want to be able to log back into my account.
- I want to be able to see that characters that I have made, then edit/delete them.
- I want to save characters that other users in the database have made. 
- I want to be able to sort/search for specific characters to fill my needs.

#### A User already with Dungeons and Dragons (D&D) knowledge
- I want to create, edit and share characters that fit within the D&D specifications. 
- I want to see new and unusual characters that people have created that I can bring to my games.
- I want to see information on characters that I can use in my games, and get ideas for characters I would like to play.



### Strategy
- The aim of the website is to provide users access to a database of characters to pick and choose from to take to their D&D games.
- The site allows users to create, edit and save characters with information such as 'Name', 'Class' and 'Race'.

### Scope
- Provide the user with a place to create, share and edit characters.
- Provide visitors with a clean and easy-to-navigate user interface.
- Allow users to sort through the characters available. 
- Provide users with the information they would need to use the characters in a game.

### Structure
#### Interaction Design
- Create a website that is responsive, works at all screen sizes and has mobile, tablet and PC compatibility.
- Allow for easy navigation between pages of the website.
- Create easy to use and understand forms for users to fill in.
- Display created character information in an easy-to-read format.
#### Information Architecture
- Content is well structured, in line with the theme, easy to read and distinguish between.
- Content is spaced evenly and consistently throughout all screen sizes. 

### Skeleton
#### Wireframes

![Wireframes](/static/images/wireframes.jpg)

#### Information Design
- Information text is separated and spaced-out to keep it clear and easy to read.
- Information and forms with images in the background are also placed on a darker background with lighter text, to help it stand out.
- All navigation links are easy to read and see.
- All forms have appropriate labels so the user knows what they need to input.
- Created character information is labelled and spaced well on all screen sizes.

#### Interface Design
- The content is spaced well, and its obvious where to proceed onto other pages on the site.
- All buttons are labelled and spaced well, so the user can see what page they will be sent to.

#### Navigation Design
- Navigation is located at the top of the page, the links the user will see is determined by their login status.
- The user can also navigate using call to actions, or will be redirected after completing certain forms within the site.

### Surface
#### Typography
Two different fonts have been selected for use on this site. Both fonts have been obtained from [Google Fonts](https://fonts.google.com/).
- Raleway: Has been used for all text that is not a heading. This font is well spaced and easy to read with a more curved style.
- Cinzel: Has been used to all headings, a sharper text easy to read with a more fantasy style to fit the theme.


#### Colour Scheme

![Colour Pallet](/static/images/thedrunkengoblinpallet.jpg)


## Features
- The site is a multi-page site that includes a Home/Landing page, where the user and view the main page of the site the 'tavern', register an account or login.
- The 'Tavern' page is the main page of the site, where all characters within the database are displayed. The idea is to display enough information for the user to 
    be able to use the characters in a game of D&D.
- There is a login form on the landing page, where the user will be 'logged in' and re-routed to their profile page.
- The profile page displays the characters the user has created, also showing the characters the user has saved.
- The create page is where the user can create a character of their own, where they will complete a form with character details and upload an image of their character.
- The edit page is a close mirror of the create page, although the placeholder text will be shown as the details of the character chose to edit.
- The user can also log out and use the site to see all characters created but will not be able to create, edit or save characters.
#### Existing Features 
- Create- The user can create an account, where they can login, view and experience the site with more features than a user without a login.
    - The user can also create characters of their own, where they can choose the; name, image, race, class, likes, dislikes and backstory all in line with D&D rules.
- Read- On the tavern and profile pages, the user can see the character information of created characters straight from the database.
- Update- Users can edit characters they have already created by selecting them from the user page.
- Delete- Users can also delete characters they have created, although not characters made by other users.
- Image upload- Upon creating a character, the user will be required to upload an image.
    - The image is uploaded to 'cloudinary' using an API within the code. 
    - This image is then edited to a specific height and width and then converted into a url.
    - This url is saved within the database in the character section, and then loaded in the tavern and profile pages.          
- Search- The user will be able to search by character name, race and class on the tavern page.
- Save characters- Upon visiting the tavern page, the user will be able to save and store any characters they would like to quickly access.
    - These characters will be available on the users profile page under the characters they have made.

#### Features Left to Implement
- Character stats- During the D&D characters creation process, the character stats are an important part. Adding a feature where the user can change the stats of the characters they made would be a natural addition.
- Improve the character save option, reducing from two buttons to one.
- Email verification- When creating an account, the site takes the users, 'username', 'email' and 'password'. Currently the email is not used within the database.
    - Adding email verification the user can confirm they have signed up to the site and will also need to validate their email address.
- Password reset- With email verification, naturally the ability to reset the user password would be a helpful addition and improve the user experience.
- Ask user to confirm if they want to delete a character.


<a name="technologies"></a>

## Technologies Used

### Languages
- Python/Flask- Used to create all functionality of the site, all pages are rendered using flask methods.
    - Flask has also been used to connect the site to the Mongo.DB database, where all information is stored and accessed from.
- HTML- Used for all template pages for the site and then rendered using Flask. Also used for the basic form structure and validation.
- CSS- Mostly used in conjunction with the Materialize CSS library to style and structure all the pages.
- Javascript- Used via JQuery and use to activate the Materialize CSS drop down selectors.
### Programs
- VS Code: Where all coding took place.
- Balsamic: Used to create wireframes.
- Heroku: Used to deploy the site for public use.
- Git Hub: Used to host the websites repository.
- Git Hub Desktop: Used to access the repository linking it to online Git Hub profile.
- IAmResponsive: Used to test responsiveness of site.
- Coolors: Used to display colour pallet used.
- [HTML Validator](https://validator.w3.org/) - Used to check HTML code for errors.
- [CSS Validator](https://jigsaw.w3.org/css-validator/) - Used to check CSS code for errors.
- [Python Validator](https://extendsclass.com/python-tester.html) - Used to check Python code for errors.

<a name="Testing"></a>

## Testing
- Code Validators- 
- Python ![Python Validation](/static/images/pythonchecker.jpg)
    - All python code is now PEP8 compliant (29/11/21).
- HTML ![HTML Validation](/static/images/htmlchecker.jpg)
- CSS ![CSS Validation](/static/images/cssvalidator.jpg)
    - Only errors to show are with Materialise Library.


### Bugs
Form validation not displaying required characters.
- Gave text inputs a 'title' displaying what characters they could use within the input.

Error when users don't upload image when creating a character.
- Changed the input to a required input, meaning the user must create a character with an image.

User login giving error when fields are empty.
- Added required to the login input area, so the button cannot submit empty fields.

Saved character functionality available for non logged in users and giving error.
- Removed the option for save characters if the user is not logged in.

Saved character functionality not saving characters.
- Saved the name of the character to save as a new array within the 'user' database.

Saved characters not showing on profile page.
- Looped through all characters within the database, comparing the character name with the saved name in the user database, then displaying the characters where the names are the same.

### Nav Bar
- Checked that all links work correctly, taking the user to the desired page.
- Nav bar condenses to hamburger icon on smaller screen and displays correctly on the side of the screen.

### Landing
- All calls to action on landing page take user to correct pages.
- Text and images are displayed correctly at all screen sizes. 

### Footer
- All links work as intended, taking user to social media sites.
- GitHub and LinkedIn work as intended, taking user to creator pages.
- Portfolio site is a dead link, opening the new instance of the site.

### Tavern 
- Users are allowed to access this page without logging in and is displayed well on all screen sizes.
- Characters are displayed as intended, users not logged in are unable to save characters. 
- Search functionality works as intended.
- Clear button reloads the page without the search criteria.
- Logged in characters can save characters.
- Logged in characters can edit and delete their own characters, these links take them to the desired page.

### Profile
- Profile page is only available to users who have logged in.
- Shows characters the user has created.
- Shows characters the user as saved from other users.
- Links to edit and delete user characters are available.

### Create 
- All form fields are blank upon loading in.
- Drop down menus work and display correct information.
- Cannot submit new character without all fields containing information.

### Edit
- Placeholder text shows information of character to be edited.
- Submitting form without re-entering details doesn't change database data as intended.
#### Testing for re-submit (29/11/21)
- Text within edit form now auto filled correctley, no longer placeholder text.
- Form can now not be submitted without an image.
- New images are uploaded and saved correctley to websites cloudinary API and display as intend within the tavern.html and profile.html.
- 

### Devices
- Galaxy S9: Works as intended.
- Galaxy S20: Works as intended.
- I phone 6: Works as intended.
- I phone 11: Works as intended.
- I Pad:  Works as intended.
- Small screen laptop: Works as intended.
- Large screen laptop: Works as intended.
- Desktop:  Works as intended.

### Browsers 
- Firefox: Working as intended, no errors.
- Microsoft Edge: Working as intended, no errors.
- Chrome: Working as intended, no errors.
- Safari: Working as intended, no errors.

<a name="Deployment"></a>

## Deployment

### Deployment to GitHub
1. Created new file inside documents folder named "Coding Course" and within that created a file called "The-Drunken-Goblin(Milestone Project 3)".
2. Opened GitHub Desktop and selected "New Repository".
3. Gave the project name "The-Drunken-Goblin" and clicked "Create Repository".
4. Opened the repository in VS Code.
5. Created index.html and README.md pages.
6. Opened up local terminal and "Git Added" both pages.
7. Committed both pages using "Git Commit".
8. Pushed changed with "Git Push" adding my work to my Git Hub page.
9. Opened my GitHub page to see the changes.

### How to fork the project
1. Select repository you wish to fork.
2. On the top right corner of the page select 'fork'.
3. Navigate to your fork of the selected repository.
4. To clone the repository using HTTPS, click "Clone with HTTPS".
5. To clone the repository using an SSH key click Use SSH, then click.
6. To clone a repository using GitHub CLI, click Use GitHub CLI, then click the clipboard icon for copying the URL to clone a repository.
7. Open Git Bash. Change directories to the location of the fork you cloned.
8. Type git remote -v and press Enter. You'll see the current configured remote repository for your fork.

### Deployment to Heroku
1. Created account on heroku.
2. On the right hand side of the screen selected 'new' drop down menu then selected 'create new app'.
3. Entered an app name and selected create app.
4. Selected Connect to git hub.
5. Entered the name of the repo from GitHub I wanted to use.
6. Once linked to git hub selected 'settings'.
7. Selected 'reveal config vars'
8. On the config vars menu added all my environment variables including secret key.
9. Selected 'deploy' from menu and enabled automatic deploys.
10. Site automatically deploys when new code is pushed up to GitHub.
11. Selected 'open app' in the top right corner to view live site.

<a name="credits"></a>

## Credits

### Technical
- Google Fonts: Used for both fonts within the site.
- Font awesome: Used for all icons within the site.
- Code Institute Task Manager Project: Provided me with basic ideas and how to format my python/flask code. 
### Content 
- Dungeons & Dragons Player's Handbook: Uses for character 'race' and 'class' information.
- Users: Creating the characters and filling the database.
 ### Images
Landing
https://i.ytimg.com/vi/hWPPD5ww0eA/maxresdefault.jpg
https://external-preview.redd.it/1no2NdmVJeE2M84ApL2X4Pb3Zh_tVpn2hYSZSSMhNqU.jpg?auto=webp&s=3fe9882592bef2e4f24b22124aed13a0b6fc3904

Register
https://static.pressakey.de/gfxgames/Pathfinder-Kingmaker-4865-1591870547.jpg

Tavern
https://images.squarespace-cdn.com/content/v1/5bd88db093a6320f071b1a50/1588853697418-KDEWXMDNH4SMZPDGZMY7/Tavern%252Bart.jpg?format=2500w

Profile
https://lh3.googleusercontent.com/proxy/Qz9EHpDUJcC35E7aTTJigzTekJ0jzJ5GjskGN3CIH0oGGg5DxtcRPE5MpPzFNn22HmdhQrS_Jmk-J1n_gPm1AH1g04sdI6Y1Vyb_g22xpKVWJfDt_df_sPNP4b9-ropnTX4

Create/Edit
https://thenerdd.files.wordpress.com/2019/11/ghostsdragonspear1.jpg

 ### Acknowledgements
- Code Institute - Running the course and providing this opportunity. 
- Maranatha Ilesanmi (Mentor) - Feedback and support during the project. 
- Slack Community - Peer reviewing my work. 
