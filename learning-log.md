# Learning AI and Business automation using Python

This journey is meant to take me from beginner to experienced Python developer and hopefully even become something successful. The idea for this journey is simple - start from Python basics and move to advanced topics like AI, automation, etc.

The goal is to develop skills enough to build automation tools for local businesses and earn income from these tools and projects.

And I believe that if I document this, then I would be more motivated to keep going building projects and better understanding my own journey. I will be honest - I have no idea what will I do with this document after I am done. Maybe I will make it public and available for others. Maybe I will keep it private. I guess we will see.

So this journey is made using AI. It is split into chapters. Each chapter has things to learn and projects to build. And I will try to explain each project - the idea of the project and what am I doing to build the project.

## Chapter 1: Python Basics

I have learned basics of python programming. Altough it wasn't too difficult because these are the same for most programming languages. This includes basics like variables, conditionals, loops, lists, etc. And I guess these are the most fundamental of any programming languages.

I guess for now most difficult for me was the file handling as I haven't worked with files previously with python programming language. This means the file handling in general, not data reading from files. I have not touched that topic yet, that is still to come. One more thing which I struggle with the most is consistency. For example one day I am pretty motivated to write some code, then I write maybe for few minutes or few lines, and then my motivation disappears and I could say that it disappears for multiple days, if not for a whole week. In my opinion if I fix the consistency issue then I could learn python pretty quickly and start actually producing value to companies.

Now moving on to projects. I have already built the first three projects so they may not be as descriptive since I do not remember perfectly what was my idea for using the tools I used. But starting with the 4th project it will be descriptive - with criteria, the reasoning for using the tools I used, etc.

### Project 1: CLI Expense Tracker

The idea was very simple. Use lists to store the expenses and user can manipulate with this array by adding/removing or editing expenses. At first I thought that good idea would be to use a dictionary, but then I had some issue with it, i don't remember it exactly but I think it was something to do with calculating total expenses. And then I simply switched to using singular list of objects like so: 
```
[{expense_name, amount}] 
```
and this way I could calculate total expense amount.

At first the code was very singular and it repeated itself a lot, for example viewing the list of expenses before adding or removing expense. So I built 4 functions at first - viewing expenses, adding expenses, removing expenses, updating expenses. And after a while I decided to add the 5th function - calculating total expenses. I realize that theoretically this is a small project and I could have gone without but I want to practice writing clean code so I tried to build this as a senior developer.

The most difficult things for me were working with arrays, especially the update function.

### Project 2: File Organizer

At first this project scared me a little and it took some time to start working this project. The idea of working with files sounded a bit advanced to me, and I have no idea why. Because when I started building this it went pretty smoothly and almost with no issues.

The idea of the project is that it organizes files from a directory into multiple directories. I feel like this is the project where AI would thrive but since that is little beyond my skills I simply organized files based on extensions, for example jpg, png files goes into Images directory and so on. And I do realize that there are too much extensions, so I just used most commonly used extensions. The workflow of this project is following: the program runs through the directory and all of its files, after that it checks the extension. Let's say that the extension is .mov and then the program checks whether the directory for this extension exists and creates it if it doesn't exist. And then after that the file simply gets moved to the directory. And the directory deciding was based on the list of extensions hard-coded into a list. I believe that for learning purposes it is fine. And even if the extension found didn't exist in the list, then it would simply be moved to miscellaneous directory. And the found directories that were inside the to-organize directory were simply skipped.

The most difficult thing for me I guess were working with modules that needed to be imported and reading through the documentation and finding the needed function for my situation. This wasn't impossible but comparing to simply writing basic python code this were a little more complex.

### Project 3: API Data Collector

This was pretty confusing as I didn't know what it meant, so I figured it meant simply get the data from third-party api and then handle it. This was pretty easy as it should be. For this project I also created virtual environment and learned about pip and packages, because I needed to install `requests` packages to get the data from the API. After that I simply chose the weather API and defined the base URL and then using that URL I requested weather data in Riga and then displayed it in the CLI.

The issue I faced with this is finding out what was inside the response and then how can I process that response and show it to the user. For example showing temperature went something like this:
```
# Get the data
r = requests.get(api_url)
temp = r.json()[0]['temp']

# Then show it to the user
print(f"Current temperature: {temp} degrees celsius")

```
It is not too complicated but compared to everything else in this project this was the most complicated issue I faced.

### Project 4: CSV/JSON Data Processing Tool

Now we are all caught up and I haven't started this project yet and I figure that maybe documenting as I go through this project would be helpful for me.

This project will be the project where I start using version control using `git`. I probably will set the repo to be all python learning projects and call it something like python-lab. For the first 3 project singular file was enough, but moving on I will create subfolders for multiple file usage.

**Criteria for the project**

I think before building this project is a good idea to set up the criteria for this project.
1. Using environment variables, user should enter password (defined in the environment file) to see the data. User gets 3 attempts to enter the password. If 3 times entered incorrectly then the program exits.
2. The program takes a CSV or JSON file as an input.
3. Let's say the data is about weekly finances (income and expenses) throughout the year, so ideally 52 records. There can be missing data or data which is not correctly formatted, for example some string where it should be number.
4. Program prints the overview of the file for user (e.g. 52 records processed, 43 records successfully processed) And output the reason for failed records (missing or invalid format). Program automatically groups the data into months (4 weeks = 1 month) and outputs it to user.
5. After the program has printed out the monthly overview user is given the choices (should be available from different file):
    - Exit the program.
    - Calculate total money from the file.
    - Calculate total money from user-chosen period (e.g. week 10 - week 48).
    - Show weekly view of the finances.
6. While building this project use `git` for version control with descriptive commits and multiple branches.
7. Write at least 5 tests for this program.

**Building the project**

Before actually building anything let's initialize the repository with `git`

Now I have initialized the repository or for short repo, and we can start building.

After the criteria is written we can start building it. I probably won't go into too much detail but I will try to explain what am I doing and why am I doing it.

This project will be inside a seperate directory as it will consist of multiple files.

The first step probably should be getting the CSV/JSON file and read its contents. Theoretically I could hard-code the file, but I will get the file from command line when starting the program. Ideally something like this:
```
py csv-json-tool.py data.csv
```
This way the program is more dynamic and can work with different files and I wouldn't need to change the code too much. 

I have built a program which takes a path command argument, then it checks if it is a valid CSV file. And after that it reads the file. The CSV file I will be using is AI generated with some of the fields missing or incorrectly formatted as I want to practice working with incorrect or missing data.

And I feel like this is a good time for a commit to `git` repo:
```
git add .
git commit -m "Program can read CSV file from command argument"
```

After this I added authentication if it can be called that. Basically it asks user for a password 3 times using a `for` loop and then compares it to the password defined in the `.env` file. For this I needed to install and import a `dotenv` package. And then again time for a commit.

Next I grouped the weeks by months. And this wasn't as easy as it sounds, because there are 52 weeks in a year, and if I take 4 weeks per month then it would turn out to 13 months which obviously is not true. So in the end I decided to consider that 4 months will have an extra week, which still is false, but I think this is better than having 13 months.

Speaking practically I created dictionary with months as keys and empty lists as values. After that I created a list for weeks per month. And then I checked for missing data in the amounts or if there are 0 misplaced with O. If there were any of these then I simply changed the amount to be 0, which possibly can lead to incorrect data, but we will see past that as this is a learning project. And then simply speaking I went through the lines in from the CSV file and then added them to the respective month - first 5 lines to January, next 4 to February and so on.

After they were added I coded a small output test to see if it is working correctly. The test simply prints out all amounts of incomes or expenses and then calculates the total and prints that out too. I calculated manually and the program worked as expected. 

For me this was quite difficult as it introduced a lot of work with lists and dictionaries which I struggle with as there are a lot of methods which I am not aware of. So this is something I have to improve.

But anyway, it is time for a commit again.

Next I decided to work on the overview of the processing. To show successfully processed rows - everything was correctly formatted and no data was missing. And also show how many rows failed to process. Currently it checks only the `amount` from the CSV.

I will commit this small change even it is not completely finished. I figure that I will upgrade this as I keep building this project.

Next up is what sounds like a simple feature - calculate the total for the whole year. This will probably be a function inside the `utils.py` file. 

Most of the function came from the already existing test that I was using before. I just had to change to check the casing too and ignore if the type is missing since that can drastically affect the data. And the program lets the user know that the type was missing for a specific week.

After the total for the year I decided to change how the monthly overview was shown. Instead of showing data for each week, which I guess sounds more like a weekly overview, I now show total calculated for each month and print it out. It simply sums the weekly amounts taking the type into consideration and then it prints out the type and the total amount.

Now that the program has multiple functionalities, I decided to build the menu to keep the CLI relatively cleaned up. This was done by making a new function `display_menu` which prints out the menu and then asks for user input and then it simply returns that input. And then in the `main.py` file it takes the user input and runs through the `match` statement. Currently it has 3 options - calculate total year amount, print the monthly overview and exit. But based on the defined requirements it will have 2 more options - showing the weekly view and calculating the money for user-chosen period.

Also the file itself has more fields like category, payment_method and description, but I haven't figured out if I am going to be using those. Maybe I will use categories field which could show money spent or earned by category. But this will be for a later time to decide.

As for now I will make a commit to repository.

Next up which was quite easy was the weekly view. Since in the file each row already was meant a week, then I simply printed out each row. But I added a month name too for better reading. I also decided to display the week number, type, amount and category since it was already there.

And for user to be able to access this feature, I added it to the menu.

Now it is time for another commit.

Personally I thought it would take me much longer time to make the last feature - user defined period calculations, but it didn't take me long at all. And I believe that this project is now done. 

I simply asked the user input for starting and the ending period, and then compared the weeks against it and showed only those who were inside the defined period, the rest of the weeks I simply skipped.

And it is commit time again.

Since this feature wasn't in the requirements then I created a seperate branch for it in case I couldn't be able to finish it. The feature I am talking about is show finances grouped by category.

But I was able to finish it. I created an empty dictionary with the category as a key and empty list as value. Then I went through the records and checked if the category doesn't exist and if not then added to the dictionary. And then I added all the amounts to the list for the respective category. And finally I looped through the made dictionary and calculated the finances for each category. And for the user to be able to use this feature I added it to the menu. 

After verifying that everything works as it is supposed to work, I can make a commit and then merge the branches.

I didn't think it would be that easy, but now this program also supports JSON format. Probably it helped that the format was similar to the CSV, where each row was the same as each object in the JSON format. 

To achieve this I simply moved the already existing code which prepared the CSV file to `utils.py` file and defined a function which takes a file and the file extension as arguments. And then simply loads data based on the extension. And then the logic for preparing the data remained the same for both - CSV and JSON files.

I wanted to do a seperate git branch for this too, but I forgot. But I believe that I will have plenty of opportunities to work with branches, so for now a simple commit to the main branch.

And finally I have written the tests for this program. This took some figuring out but in the end I managed to write 5 tests. I realize that there probably is much better way to write the tests I wrote but this was an intro to software testing using pytest and I am glad that I am a bit more familiar with this now.

Also I realized that I haven't added the files I used for data in this project. Now they should be added to the project.

And with this I can finish this project and this was the final project of the chapter 1 of this roadmap. I can say that I am quite comfortable with python basics and can build simple CLI programs. Of course I could spend more time in this chapter but I believe that these basics will be used over and over. After making the last commit for this project I will be moving on to chapter 2.

## Chapter 2: APIs, Webhooks & Internet Systems

The theory of this chapter is mostly clear to me. I would have to learn or establish things like API keys, Bearer tokens, OAuth 2.0 and JWT concepts, webhooks, payload validation, signatures, retries, idempotency, pagination, rate limits, API errors, API documentation. These things aren't unfamiliar, but I don't understand them perfectly.

And the project also sounds quite confusing to me. It looks like it should be built by using some kind of web framework, but I don't see the place for web framework in this roadmap.

After consulting with AI, I think I understand know. I will have to simulate the lead by using a JSON file. Then I validate it, clean it, transform it if required and then I save it to a CSV file. And after it has been saved I send a notification, but in this case I will probably just simulate it.

But I just have to figure out how to connect the theoretical things with this project.

I probably won't be needing any of the security tokens for this projects so I will simply study and understand the concepts of that. But maybe I could integrate some sort of check for security - maybe a kind of password which is given when user authenticates, but I am not sure yet.

Here is what I am thinking so far... I will create a JSON file to simulate the lead. Then I will validate it and prepare it for storing. To store this lead I will create a CSV file and append each lead to that. And once the lead is successfuly added to the CSV, a webhook will be triggered which will send the notification, that a new lead has appeared.

But I still have no idea how would I use the signatures, retries, rate limits, API errors/documentation. Maybe I will figure that out as I start building the project.

So here is everything I will learn and use in the project most likely:
- HTTP requests and responses
- GET/POST request methods
- Headers, body, status codes
- Webhooks, payload validation, retries, idempotency (every identical request produces the same result)
- API errors and API documentation.

### Project: Business Lead Intake System

It is time to start building again. To start, I simply made 3 lead JSON files, example:
```json
 {
  "name": "Alex Johnson",
  "email": "alex@example.com",
  "company": "Johnson Plumbing",
  "service": "Website automation",
  "message": "I want to automate customer inquiries."
}
```
Then I read from this JSON file and create, if it doesn't exist already, a CSV file where all leads will be stored, and store the data inside the CSV file. This will be the base code which will be upgraded into a fully working system.

I just wanted to code a small version which I know works correctly.

Small update: I added a `validator.py` which will validate the JSON file before writing it to the CSV file. Later on this validator most likely will also validate the webhook before sending it.

And then I created an invalid lead file `lead-invalid.json` where I tried all possibilites where the validation should fail and it worked successfully.

Now I have worked on the webhook and I believe that it is working properly now. The tought at first was to create a new web server using python and then handle the request using probably something like FastAPI, but that will be learned at a later chapter, so I used already existing Laravel projects I had and defined a new route there.

For the webhook I created a new file `webhook.py` and in there a function `trigger_webhook` which tells the user that the webhook has been triggered and then it sends a post request to the Laravel project and it also sends over the data - event, which in this case it is `lead.created` and also the lead itself. This function gets called right after adding the lead to the leads CSV file.

And probably this will be it for the webhook. I just wanted to see and understand how the webhook worked and I think that I do now. Of course this webhook doesn't do anything useful, but the idea is that it can do something like sending the notification, but I didn't want to do that using Laravel, that is why I am calling this done.

I did a code review with AI and it found quite a few issues with my code. Some might be critical to the functionality of the app. So I decided to build a new project. It still will involve webhooks, requests, etc., but this time I will spend more time on it and making sure it is secure and it also handles errors. At least that is the plan.

### Project: Business Order Status Webhook System

The project I will be building is Business Order Status Webhook System. The idea was generated by AI and it simply allows user to change the status of an order and then the product detects that change has been made and then the webhook gets triggered. I still probably will use the already existing Laravel project.

Also I organized the repository a bit. Now each chapter is sorted into its own seperate directory. I am still not sure what to do with this `learning-log.md` file... Should I also seperate it into the overall which will be located in the root of repository, and then each chapter gets its own learning log. Or should I simply leave it as is. For now I will leave it as it is and I will think about that.

Going back to the project, let's define the core functionality, let's plan where each functionality will be located at and what will the structure of the project look like.

The structure I am thinking something like this:
+ business-order-status-system
    + main.py
    + utils.py
    + webhook.py
    + orders.json

And it looks like that is it. `main.py` will be responsible for displaying the UI in the CLI and calling the required functions from `utils.py` or `webhook.py`. `utils.py` will have the utility functions like `show_current_status()`, `change_order_status()`. `webhook.py` will be responsible for sending the webhook to the Laravel endpoint. And finally the `orders.json` file will store the orders.

I have written a starter program without webhooks for now. Currently it simply reads the JSON file and allows the user to change the status. Later on I will add more error handling and webhook itself as currently it only checks if given file exists and if it is a JSON file.

I have added error handling for the current version of the program. It now checks whether the orders have any missing values. When selecting order user must input a valid ID from the available orders, otherwise the program catches that. And same thing is for the update function. It has to be a valid integer input. And also if the selected status is the same as already existing one then it simply exits, as there is no reason to update the file. And I am not aware of what type of errors could occur while updating the JSON file, I just handled it as a general Exception. All this was inside the `utils.py` file.

And in the `main.py` file I first of all check if the file is provided. After that I check if the file was read successfully, if not, then it simply quits with message. This could happen if any values was missing and the `read_orders()` function returned failure. But if successful then it puts it in the variable which is used for other functions. And if the user entered invalid ID for order then it simply prints that program failed to select an order and exits. But if it was successful then it moves on to status changing, where the function `change_order_status()` returns an object with keys `success`, `changed`, `message`. As you can probably guess the order file only gets updated if `success = True` and `changed = True`, otherwise nothing happens. And if nothing gets returned then that gets handled also simply by printing out a message.

And finally which I think is the most important part of this project is the webhook itself. This time it has retry system made by using a simple `for` loop. Also it has a signature made using modules `hmac` and `hashlib`. I am using `sha256` encoding. From what I gathered I encoded the secret key and the payload to bytes. And then the Laravel project had the same secret key and then it built a hash and then compared it with the hash generated in the python project. And if these hashes were the same then everything worked properly and only then it returned that webhook was successful.

## Chapter 3: SQL & PostgreSQL

The chapter 2 of AI automation roadmap has been finished and now it is time to move on to the chapter 3 - databases, SQL - specifically PostgreSQL.

I already have studied the theory - the basics I learned in university I only reviewed, but the concepts that I had to study more in-depth were normalization, indexes, common table expressions (CTEs), window functions and transactions. These are fairly complicated things, so I will revise them as I keep building projects that uses databases.

### Project: Lead Management System

So now it is time for the project of the chapter 3. This project is similar to the Business Lead Intake System, only this time the leads will be stored inside a database instead of CSV file. And user will be able to do CRUD operations - create, read, update, delete.

First things first I will create an empty database and then connect to it with Python. For this I will probably use `.env` file to store the database credentials. And then the connection will be made inside `database.py` file to keep thing organized.

The database is created and the connection has been made. I created the database using GUI tool `pgAdmin 4`. I also created a separate database user that can access only this database for security reasons. And then I defined the connect function inside the `database.py` file and called it from the `main.py`.

And to test if the connection works I executed this query:
```sql
SELECT version();
```
and it returned:
```
[('PostgreSQL 18.6 on x86_64-windows, compiled by msvc-19.44.35229, 64-bit',)]
``` 
so I can verify that the connection indeed was successful.

I have implemented 2 features - you can get all leads from the database, and you can create a new lead.

I have created a `menu.py` file which prints out the menu and gets user input from it and returns it. Also I created a `leads.py` file where all the CRUD operations will live as a separate functions. 

Also I read that I should close the cursor and database connection when I stop working with it so I added a `disconnect(connection, cursor)` function which does exactly that - closes the cursor and the database connection.

After some work I have added update and delete functionalities as well. Now the program has available all CRUD operations. For now this is the base we will work on. I want to implement features like sorting by id or date (for this I would need time as well as it is not showing currently), search function that allows to search by lead name, customer name. These features most likely will be added on the next commits. And also I need to think about the error handling which I have not implemented, e.g. database connection failure, query failure, etc.

I have added the sorting functionality. You can sort by all fields in ascending or descending order. This wasn't as easy as it sounds, because first I tried to parameterize queries like so:
```python
cursor.execute(query, (parameters))
```
but this didn't work because in the parameters were defined strings with the quotes and quotes were inserted in the query too and that broke the query. So the solution was to use the `sql` module from `psycopg2`. I created the query in a variable with following structure:
```sql
query = sql.SQL('query {} {}').format(parameters)
```
This way I define where the parameters should go and then I provide the parameters themselves. And I guess the format() removes the quotes, because this way it worked successfully.

It turns out that the example above is not safe and vulnerable to SQL injections so that had to change, because `sql.SQL(query)` doesn't do any type of validation or escaping. I had to basically combine both examples to something like this:
```sql
query = sql.SQL('query {} %s').format(parameters) -- pass safely handled identifiers
cursor.execute(query, (parameters)) -- pass the untrusted values here
```
I changed the `view_sorted()` function and considered this when I created the `search()` function, which I successfully created and took some time because the search query was different for the ID and the date fields. I decided to use the if..elif..else statement to check which field was selected and then the query gets built accordingly.

I have added error handling for this project. It handles database connection failure, correct value types should be entered in the menu, handles failed attempts to find non-existing attempt, if something is not found, then the program does not crash. And with this the project should be complete more or less. Of course there are many ways this project could be better, but for learning experience I think it is enough as I learned how to work with database using python.

I will now commit this and then do a code review with AI.

AI found some issues and bugs in my code. The issues found and fixed:
- Database connection string was printed out to terminal. Credentials were not validated. Switched to keyword credentials instead of string. Add error handling for database connection failures.
- Added validation for empty fields when creating leads. Prevented the application from inserting incomplete records. Added validation for user-provided lead IDs. Checked whether a lead exists before updating or deleting it. Added confirmation before deleting a record. Improved error handling around INSERT, UPDATE, DELETE and SELECT operations.
- SQL injection prevention
- removed redundant try..except blocks.
- proper transaction handling.