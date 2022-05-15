# Football Nerds FC
[View the live project here.](https://football-nerds-fc.herokuapp.com/)

Football Nerds FC is a Python command-line/terminal game, which runs on Heroku.

It’s a multiple choice football quiz – the user has to try and answer ten football-related questions randomly picked by the app, with the final score being presented to the user at the end. There are three answers for each question (1, 2 and 3), but only one is correct. Find out if you have what it takes to be the football nerd of the day!

## User Experience (UX)
### User stories
#### o	First-time Visitor Goals

**a.**	As a first-time user, I want to easily understand the main purpose of the game and how to play it.

**b.**	As a first-time user, I want to navigate through the game with ease without encountering any error messages or getting stuck.

**c.**	As a first-time user, I want to be able to test my football knowledge and answer correctly to as many questions as possible.

#### o	Returning Visitor Goals

**a.**	As a returning user, I want to play again and try and answer different football questions to further test my football knowledge.

#### o	Frequent User Goals

**a.**	As a frequent user, I want to play again and again to try and answer all the football questions of this game to fully test my football knowledge.

## Flowchart

Flowchart – [View](assets/flowchart/flowchart-football-nerds-fc.jpeg)

In order to better visualize the steps required to build and play this game, I created a flowchart using Lucidchart, which allowed me to go through each part step-by-step and to understand what objects, features and functionalities were necessary and how to code them based on the user’s potential needs while using the app at every step of the way.

## Features

•	It works on all device sizes, but it's not responsive on all device sizes: it's a Python command-line app built using Python alone, so no HTML, CSS (media queries would have been used if it was a website, for example) or JavaScript were used, which is why it may not be fully responsive in smaller devices (tablets, smartphones, etc.).

**•	Welcome Message**

o	It welcomes the user to the game, explains its nature and challenges the user to play and be a true football nerd.

[Screenshot of the welcome message here](assets/docs/welcome-message-screenshot.png)

**•	Questions**

o	A list of 80 questions was created for this game, and the app randomly picks 10 as a sample of questions to be asked to the user every time a new game starts. The user is provided with 3 potential answers for each question, but only one is correct, and it's up to the user to guess the correct one. When the user gets it right, a "correct" message comes up informing the user that he/she got it right:

[Screenshot of the message when the user chooses the correct answer](assets/docs/question-answered-correctly-screenshot.png)

o	When the user gets it wrong, an "incorrect" message comes up informing the user that he/she got it wrong:

[Screenshot of the message when the user chooses the incorrect answer](assets/docs/question-answered-incorrectly-screenshot.png)

**•	Input Validation and Error-handling During the Game**

o	If the user inputs invalid data (any other input other than "1", "2" or "3"), an "invalid data" message comes up informing the user that he/she inputted invalid data and prompting him/her to re-enter valid data (he/she cannot proceed from the current question until valid data is inputted):

[Screenshot of the message when invalid data is inputted – Questions – example 1](assets/docs/example-of-invalid-user-input-and-validation-screenshot-1.png)

[Screenshot of the message when invalid data is inputted – Questions – example 2](assets/docs/example-of-invalid-user-input-and-validation-screenshot-2.png)

[Screenshot of the message when invalid data is inputted – Questions – example 3](assets/docs/example-of-invalid-user-input-and-validation-screenshot-3.png)

[Screenshot of the message when invalid data is inputted – Questions – example 4](assets/docs/example-of-invalid-user-input-and-validation-screenshot-4.png)

**•	Final Result and Congratulations Message**

o	When the user answers the last of the 10 questions, a message with the result (for example, 4/10 answers correct) is displayed to tell the user how he/she did, followed by a message congratulating him/her:

[Screenshot of the message with the final result and the congratulations message](assets/docs/final-result-and-congratulations-message-screenshot.png)

**•	Play Again Option**

o	At the same time as the final result and congratulations message, a message giving the user the option to play again is displayed – if the answer is "y" (yes), the app will choose another random sample of 10 questions and the game restarts with the first of those 10 questions:

[Screenshot of the message when the user chooses to play again](assets/docs/play-again-yes-screenshot.png)

o	If the answer is "n" (no), a "thank you for playing" message is displayed and the game is over:

[Screenshot of the message when the user chooses not to play again](assets/docs/play-again-no-screenshot.png)

**•	Input Validation and Error-handling for the Play Again Option**

o	If the user inputs invalid data (any other input other than "y" or "n"), an "invalid data" message comes up informing the user that he/she inputted invalid data and prompting him/her to re-enter valid data (he/she cannot proceed from the play again option until valid data is inputted):

[Screenshot of the message when invalid data is inputted – Play Again Option – example 1](assets/docs/example-of-invalid-user-input-and-validation-screenshot-5.png)

[Screenshot of the message when invalid data is inputted – Play Again Option – example 2](assets/docs/example-of-invalid-user-input-and-validation-screenshot-6.png)

[Screenshot of the message when invalid data is inputted – Play Again Option – example 3](assets/docs/example-of-invalid-user-input-and-validation-screenshot-7.png)

[Screenshot of the message when invalid data is inputted – Play Again Option – example 4](assets/docs/example-of-invalid-user-input-and-validation-screenshot-8.png)

### Features Left to Implement

•	Username input

•	Showing the correct answer when the user gets the answer wrong

•	A scoreboard/leaderboard with the highest scores ever to be shown at the end of each game

## Data Model

Not all things can be represented using, for example, strings, numbers or Booleans. Some things cannot be covered by the data types available in Python (or in any other language), which is why we should use classes and objects to create our own data types whenever necessary. I wanted to use Object-Oriented Programming (OOP) for this simple football quiz, so I created a class called "FootballQuizQuestion", which stores all the attributes a football question should have – it's a template for what a football question should be. This class contains an Initialize function, to map out all the attributes of a football question. In this case, it stores the question's prompt and the answer (its attributes), all the information we need to create the many question objects to be used by this app. When the game is first ran, a football question prompt is retrieved from a .json file, and this prompt is then passed as a parameter when creating the question object. The user is then prompted for his/her first answer, which will be validated/handled accordingly, and the game runs its course. This data model seemed appropriate for this kind of game.

## Technologies Used

### Languages Used

•	[Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries & Programs Used

1.	[random Python package](https://docs.python.org/3/library/random.html):
o	Python's built-in random package was imported so the sample method could be used to retrieve a sample of ten questions from a .json file every time a new game starts.
2.	Snipping tool:
o	A snipping tool was used to create all the screenshots on this README.md file.	
3.	[Git](https://git-scm.com/):
o	Git was used for version control by utilizing the Gitpod terminal to commit to Git and push to GitHub.
4.	[GitHub](https://github.com/):
o	GitHub is used to store the project's code after being pushed from Git.
5.	[Heroku](https://dashboard.heroku.com/apps):
o	Heroku was used to deploy the live project.
6.	[Lucidchart](https://lucid.app/documents#/dashboard?folder_id=home):
o	Lucidchart was used to create the flowchart during the design process.

## Testing

PEP8 Online Checker was used to validate all the code on the Python file for this project to ensure there were no syntax errors.
•	PEP8 Online Checker - [Results](assets/docs/pep8-online-results.png)

The [Am I Responsive?](https://ui.dev/amiresponsive) website design tester was used to test the responsiveness of this website (though, as mentioned on the "Features" section of this README.md file, this app works on all device sizes, but it's not responsive on all device sizes – it's a Python command-line app built using Python alone, so no HTML, CSS [media queries would have been used if it was a website, for example] or JavaScript were used, which is why it may not be fully responsive in smaller devices [tablets, smartphones, etc.]). [Screenshot here](assets/docs/am-i-responsive-results.png)

Testing User Stories from User Experience (UX) Section
•	First Time Visitor Goals
i.	As a First Time Visitor, I want to easily understand the main purpose of the site and learn more about the organisation.
a.	Upon entering the site, users are automatically greeted with a clean and easily readable navigation bar to go to the page of their choice. Underneath there is a Hero Image with Text and a "Learn More" Call to action button.
b.	The main points are made immediately with the hero image
c.	The user has two options, click the call to action buttons or scroll down, both of which will lead to the same place, to learn more about the organisation.
ii.	As a First Time Visitor, I want to be able to easily be able to navigate throughout the site to find content.
a.	The site has been designed to be fluid and never to entrap the user. At the top of each page there is a clean navigation bar, each link describes what the page they will end up at clearly.
b.	At the bottom of the first 3 pages there is a redirection call to action to ensure the user always has somewhere to go and doesn't feel trapped as they get to the bottom of the page.
c.	On the Contact Us Page, after a form response is submitted, the page refreshes and the user is brought to the top of the page where the navigation bar is.
iii.	As a First Time Visitor, I want to look for testimonials to understand what their users think of them and see if they are trusted. I also want to locate their social media links to see their following on social media to determine how trusted and known they are.
a.	Once the new visitor has read the About Us and What We Do text, they will notice the Why We are Loved So Much section.
b.	The user can also scroll to the bottom of any page on the site to locate social media links in the footer.
c.	At the bottom of the Contact Us page, the user is told underneath the form, that alternatively they can contact the organisation on social media which highlights the links to them.
•	Returning Visitor Goals
i.	As a Returning Visitor, I want to find the new programming challenges or hackathons.
a.	These are clearly shown in the banner message.
b.	They will be directed to a page with another hero image and call to action.
ii.	As a Returning Visitor, I want to find the best way to get in contact with the organisation with any questions I may have.
a.	The navigation bar clearly highlights the "Contact Us" Page.
b.	Here they can fill out the form on the page or are told that alternatively they can message the organisation on social media.
c.	The footer contains links to the organisations Facebook, Twitter and Instagram page as well as the organization's email.
d.	Whichever link they click, it will be open up in a new tab to ensure the user can easily get back to the website.
e.	The email button is set up to automatically open up your email app and autofill there email address in the "To" section.
iii.	As a Returning Visitor, I want to find the Facebook Group link so that I can join and interact with others in the community.
a.	The Facebook Page can be found at the footer of every page and will open a new tab for the user and more information can be found on the Facebook page.
b.	Alternatively, the user can scroll to the bottom of the Home page to find the Facebook Group redirect card and can easily join by clicking the "Join Now!" button which like any external link, will open in a new tab to ensure they can get back to the website easily.
c.	If the user is on the "Our Favourites" page they will also be greeted with a call to action button to invite the user to the Facebook group. The user is incentivized as they are told there is a weekly favourite product posted in the group.
•	Frequent User Goals
i.	As a Frequent User, I want to check to see if there are any newly added challenges or hackathons.
a.	The user would already be comfortable with the website layout and can easily click the banner message.
ii.	As a Frequent User, I want to check to see if there are any new blog posts.
a.	The user would already be comfortable with the website layout and can easily click the blog link
iii.	As a Frequent User, I want to sign up to the Newsletter so that I am emailed any major updates and/or changes to the website or organisation.
a.	At the bottom of every page their is a footer which content is consistent throughout all pages.
b.	To the right hand side of the footer the user can see "Subscribe to our Newsletter" and are prompted to Enter their email address.
c.	There is a "Submit" button to the right hand side of the input field which is located close to the field and can easily be distinguished.
Further Testing
•	The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
•	The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX.
•	A large amount of testing was done to ensure that all pages were linking correctly.
•	Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.
Known Bugs
•	On some mobile devices the Hero Image pushes the size of screen out more than any of the other content on the page.
o	A white gap can be seen to the right of the footer and navigation bar as a result.
•	On Microsoft Edge and Internet Explorer Browsers, all links in Navbar are pushed upwards when hovering over them.
Deployment
GitHub Pages
The project was deployed to GitHub Pages using the following steps...
1.	Log in to GitHub and locate the GitHub Repository
2.	At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
o	Alternatively Click Here for a GIF demonstrating the process starting from Step 2.
3.	Scroll down the Settings page until you locate the "GitHub Pages" Section.
4.	Under "Source", click the dropdown called "None" and select "Master Branch".
5.	The page will automatically refresh.
6.	Scroll back down through the page to locate the now published site link in the "GitHub Pages" section.
Forking the GitHub Repository
By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...
1.	Log in to GitHub and locate the GitHub Repository
2.	At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3.	You should now have a copy of the original repository in your GitHub account.
Making a Local Clone
1.	Log in to GitHub and locate the GitHub Repository
2.	Under the repository name, click "Clone or download".
3.	To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4.	Open Git Bash
5.	Change the current working directory to the location where you want the cloned directory to be made.
6.	Type git clone, and then paste the URL you copied in Step 3.
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
7.	Press Enter. Your local clone will be created.
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
Click Here to retrieve pictures for some of the buttons and more detailed explanations of the above process.
Credits
Code
•	The full-screen hero image code came from this StackOverflow post
•	Bootstrap4: Bootstrap Library used throughout the project mainly to make site responsive using the Bootstrap Grid System.
•	MDN Web Docs : For Pattern Validation code. Code was modified to better fit my needs and to match an Irish phone number layout to ensure correct validation. Tutorial Found Here
Content
•	All content was written by the developer.
•	Psychological properties of colours text in the README.md was found here
Media
•	All Images were created by the developer.
Acknowledgements
•	My Mentor for continuous helpful feedback.
•	Tutor support at Code Institute for their support.
