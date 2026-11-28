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

## Chapter 4: n8n & Workflow automation

It has been a few days since my last commit. But that is because I was setting up and learning n8n automation which is the next chapter in the AI Automation Roadmap. And after doing some research I can say, that n8n is a pretty powerful tool. It is possible to automate pretty much anything. I played around a bit and built my first workflow - it takes input from form, appends it to spreadsheet and then sends an email. And I have to say the feeling was pretty amazing when I saw that email.

And setting up n8n itself was quite simple. All I had to do was run:
```sh
npm install -g n8n
```
And then run the n8n instance with:
```sh
n8n
```
Then wait for a moment and the n8n is ready for use in the browser. But a bit more complex was to set up the credentials which allows to use the API which allows to do all of the automation. But after some time I have it working.

For now I have the n8n running only locally, but in the later chapters when I will learn Docker, I will be able to dockerize the n8n and host it on the VPS I rent.

### Project 1: Automated Lead Management System

And for the project of this chapter, I have to create automated lead system. The idea I currently have is quite simple. It is going to be similar to the project of chapter 3. But this time I will focus more on n8n. Only thing that python will handle is take user input for the lead and then send an webhook to n8n where most of the flow will be automated. It will take the lead info and insert it into PostgreSQL database and then send a notification to my phone - most likely Telegram.

The complete workflow could look something like this:
#### Python
1. The user submits the lead from the CLI.
2. The lead gets validated and unique ID gets generated and the lead gets formatted as JSON. 
#### n8n
3. The lead gets sent to the n8n automated workflow via webhook.
4. Then the lead gets compared to existing leads to check for duplicates.
5. After every check is completed and no issues are found, then the lead gets inserted into database
6. When insertion was successful, I get notified via Telegram or email, that new lead has appeared.

So we need to come up with some validation rules before starting to build the project.

#### Required customer fields
- Name: 2–50 characters.
- Email: Valid format.
- Phone: Valid basic format.
- Service: Must match an allowed service.
- Message: 5–2,000 characters.
#### Required metadata
- Lead ID: Valid UUID v4.
- Created timestamp: Valid ISO 8601 timestamp.
#### Duplicate handling
- Existing UUID: Reject duplicate submission.
- Different UUID with same email: Accept.
- Different UUID with same phone: Accept.
- Same customer submitting different services: Accept.
#### Workflow rules
- Invalid payload: Stop processing.
- Valid payload: Check UUID against PostgreSQL.
- New lead: Insert into PostgreSQL.
- Successful insertion: Trigger Telegram/Email notification.
- Failed insertion: Do not send success notification.
- Failed notification: Keep lead stored and allow notification retry.
- Repeated request: Never create a second record for the same UUID.

I have built the project which once again was not too difficult. It resulted into 2 files - `main.py` and `validator.py`. I decided to do it like this since most of the lifting was happening inside the n8n. 

The `main.py` file is responsible for taking the user input, calling the `validator.py` file to validate the input, id generation using `uuid` module, and then creating the JSON payload and making a POST request to n8n webhook which triggers the workflow.

And inside the `validator.py` file the validation happens. It checks whether the required fields are present, then it checks the length of the fields. And if something is wrong then `False` gets returned from the validator and the `main.py` doesn't trigger the POST request.

And inside the n8n it first checks the PostgreSQL database to see if a lead with the id doesn't already exist. And if it exists then it stops the workflow. But if it doesn't then it inserts the lead in the database table with following fields - id_lead, name, email, phone, service, message, and created_at. The only nullable field is message. And after it has been inserted it sends an email that a new lead has been generated. And that is it. 
(Post project comment) - I actually don't know why I called it Automated Lead Management System since you can't manage the leads, you can only add them. I guess more suited name would be Automated Lead Pipeline System.

### Project 2: Automated Order Management & Fulfillment System.

I have decided that I should build a bit more complex projects as the last I built used only one database table. So the next project I will build is Automated Order Management & Fulfillment System.

This project will use multiple database tables. The automated workflow will have error handling since the workflows I have built used no error handling at all. So this is something I will have to learn.

Before building the project, let's map out what this project should solve and do. This project will allow businesses to automate order management. It could look something like this: 
- Customer perspective: there are products displayed and I can select one or multiple products with different quantities. After I have selected them the program sends a webhook to the n8n automated workflow. And there most of the heavy lifting happens. First it checks whether the products are in stock, and if not then the order gets cancelled and I get informed that specific products are out of stock. If all products are in stock then it allows me to move forward. After the order has been registered I get a notification that order has been confirmed and the status gets changed to shipped. Then after simulating some time it will get changed to delivered and I will receive another notification that the order has been delivered and it is ready for pickup.
- Business perspective: The project allows me to easily manage customer orders with little to no interaction. I will get notified that a new order has been made, I will be able to follow it (see the items, status, customer info). And I will also get notified when my inventory is getting low and I should order more (maybe I can automate this as well). I will also be able to easily track inventory changes (when user makes an order, inventory gets restocked). And I will also be able to track orders which are processing for too long to see if something has gone wrong. And also as a business owner I will be able to update stock (remove, add, change).

And this could be like a summary for the project.

Now that the idea is somewhat clear I start building it. First things I think it would be a good idea to focus on CLI side first. So first thing I will do is create the connection to the database via `database.py` file, which returns the connection and the cursor which will be used in other files.

For this I created a new `.env` file in the project folder. I am using seperate `.env` files for each project to solidify my knowledge on how to use these environment files and the variables set in them.

Next up I will create a menu, where user will be able to register either as a customer or as the business owner, then based on that the menu will change. The customer will be able to see browse products, add them to cart, and place the order which will trigger the n8n workflow. For this I probably won't use any authentification, I will just ask the user to log in either as a customer or business owner.

To achieve this, I created a `authentication.py` file, which asks user to authenticate either as a customer or business owner and then returns that type. My reasoning is, that this is quite simple way to achieve this and I realize that this is not secure way to do this, but the goal of this project is to learn and practice n8n automation.

Next up would be to show the menu based on the user type. I am thinking that a separate `menu.py` file where two menus are defined, and then the function inside this file could take user type as a parameter and then based on that return relevant menu. To achieve this I used nested `match` statements. The outer one determines the user type and asks for input, and the inner one then takes that input and then calls the relevant function. Currently it is with placeholder code.

I just realized, that I have made a mistake. I wanted to also use a database table for customers, but currently it does not have an option to use that. To fix this I will change the schema to use the user type in the table and then I will pass the type to the menu. And inside the authentication I will ask for user credentials, which I probably will store in the database as encrypted value.

I believe that I have corrected my mistake and now it is possible to create a new user and log in with that user. Currently the default user type is set to 'business', but that will change in near future. The default type most likely will be 'customer', and I am not sure whether I want multiple businesses. For now, only one business will exist.

And now after user has authentificated, the user gets returned to the `main.py` file and then based on the user type, appropriate menu gets shown.

Next I probably should display all the products. I am thinking that I should display only those products which are in stock. And then for example if the user selects a product and sets the quantity to be more than the available, then the n8n will produce the error and then I will think what to do with that. 

I am thinking that I will create separate files for functionality. Seperate for products, orders, customers. This will help me keep things organized.

The first file will be `products.py`. This file will be responsible for displaying all products, adding products to cart which I have not how that will work yet. And maybe later on some sorting or searching functionality.

While working on displaying all the available products, I discovered something which could be very useful. It is f-string formatting. I was already using these, but to just display variables. I had no idea that it can also do padding, aligning, decimal precision, and many other things. But now I do know this and I can make the CLI tables look nice and formatted.

Next up I want to implement cart functionality. At least very basic one. User can add one item to cart. I decided to create a separate file for the cart features. It is called `cart.py`. It will have functions like `view_cart(cart)`, `add_to_cart(item, cart)`, `remove_from_cart(item)`. These are the basic functions it will have. I tried defining cart as a empty dictionary in this file and then the functions would manipulate with this cart, but that didn't work. I think the cart reset on each call. So I decided to define the empty cart dictionary in the caller file, which in this case is `menu.py` and then just pass the cart object to each function.

I have built most basic and primitive cart functionality. And I do realize that the cart only exists while the python program is running, but I think that should be enough, because I only need the cart to be constructed and being sent to the n8n workflow. It doesn't have to remember what was in the cart after the program stops.

But this is not ideal as user has to manually add products to cart one by one, so I have to update it to allow multiple products. I will ask the user for multiple IDs of the products, then add them to array, and then create a new array with the items to add based on the input IDs, and then simply pass that array to the function.

Since I ask user to separate the IDs by whitespace, then I can simply use `split()` to automatically add the ID to array. Then I go over all products and compare the IDs, and if they match then I add the product to the array which is going to be sent to the function. At first it wasn't working because the IDs were not the same type. `split()` returned array of strings, but the actual products had integer IDs, so I converted them to string and then made the comparison.

This took some more time but eventually I also implemented the same functionality to remove multiple items from cart. This took some more time because I compared the IDs wrong again, but this time it wasn't a type issue but what I wrote as the ID. At first I wrote the loop like this:
```python
for product in cart:
    if (str(product[0]) in item_ids):
        print(f'Deleting item with key: {cart[product][1]}')
        cart.pop(cart[product][1])
```
And there were multiple issues with this code. And `cart` here is a dictionary with all the items, for example: 
```
{'Laptop Lenovo ThinkPad': (1, 'Laptop Lenovo ThinkPad', Decimal('899.99'), 12)}
```
And `product[0]` would return the first letter of the key, in this case 'L'. And this way it will never match what is in `item_ids` which are numbers. So the fix was to use `cart[product][0]` instead which correctly returns the ID.

And the second issue was that once I deleted something from the dictionary, it would return `RuntimeError: Dictionary size was changed during iteration` which makes sense because the iterable object is not the same anymore after deleting an item. To fix this I made a copy using `list(cart)` and the rest of the loop remained the same.

And for me to not restart the app constantly after one action, I introduced a `while(True)` loop to allow me to make multiple actions. And to simply quit the program I have to input 4 then the loop breaks.

Now I will create `webhook.py` file in which I will send the order webhook to the n8n workflow. And later on I will handle it. For now it will have a placeholder code. For now it has only one function `send(cart)` which sends prepares the payload and sends the webhook. It receives the cart and then it sends that cart to the n8n.

Additionally I made a small change to `products.get_all()` function. Before it didn't print out the products, it only returned them. But now it does both. I did this, so I did not have to repeat the printing out for business menu.

For businesses I can't yet implement view placed orders features, because that has to be handled inside the n8n. For now I can view registered customers and update inventory. And for these business actions I will create a new file `business.py`.

And similar to the customer menu, I made it loop so the program allows multiple actions in single launch. And the customer viewing is also implemented. It simply executes a sql query which returns all users whose type is `customer`, because logically I don't think it needs to see the business users as well.

Next I will implement update inventory feature. I think a good way to implement this is to create a new `match` statement inside the function which includes these options - add, update or delete. And this will have to update 2 database tables - products table and the inventory log table which tracks changes made to the inventory. 

And now to think of it the business should also be able to see inventory changes. But now the priority is to update inventory feature, which was a bit longer than expected. So in the end my decision was to make a function `update_inventory(cursor, connection)` which then asks user what he would like to do, and then based on that it calls another function - `add_product(cursor, connection)`, `update_product(cursor, connection)`, or `delete_product(cursor, connection)`. I am passing connection to these three functions because they change the data stored in the database and I am using `connection.commit()` to actually commit these changes. And to add multiple products, I am simply asking user how many products to add and then using a `for` loop I call `add_product(cursor, connection)` function. 

And when user would like to update product, then option gets presented - change name and/or price or change stock. I did this this way, because if user would like to change stock, then it executes two queries - one that updates the products table, and other that updates inventory_log table. But if the user updates only the name or price then it updates only the products table.

Next feature I will work on is the inventory change list. Since it is stored inside database table, then it shouldn't be too difficult to implement, only thing what I will have to do is display product name which is referenced. This should be possible with JOIN clause in the query.

I create a function `view_inventory_changes(cursor)` which executes a SQL query which returns results from the mentioned table and simply displays it.

At first I struggled a bit with the query and how exactly to JOIN both tables, but then I looked it up and wrote it successfully.

Another issue was with how to show whether the change was positive or negative. Because negative change was stored like this '-4', but positive was without a sign, so I wanted to include the sign as well. At first I simply tried it like this:
```python
log[1] = '+' + str(log[1]) if log[1] > 0 else log[1]
```
where `log` is a tuple representing the return row and `log[1]` is the change column. But this did not work, because in python tuples are immutable, which means they can't be changed after creation. The simple way I solved this:
```python
stock_change = '+' + str(log[1]) if log[1] > 0 else log[1]
```
This way I am simply conditionally assigning the value to variable without trying to change tuple value.

Before starting to work on n8n I should implement the product quantities when adding to cart. The way I plan to implement is loop through the items user wishes to add to cart, and then ask how many products, where 1 will be default value. And then I will add the quantity to the payload probably.

Because of the way I handled adding quantites, I had to make some changes to all `cart.py` functions. This is the way I decided to add quantities to cart:
```
{'Laptop Lenovo ThinkPad': {'Product': (1, 'Laptop Lenovo ThinkPad', Decimal('899.99'), 12), 'Quantity': 1}}
```
Each item has a dictionary object with product tuple and quantity integer. And I display values like this:
```python
print(
    f"{cart[item]['Product'][0]:0>4d}  "
    f"{cart[item]['Product'][1]:<40}"
    f"{cart[item]['Product'][2]:<12.2f}"
    f"{cart[item]['Quantity']:>8}"
)
```
And I had to change all `cart.py` functions to use this format to access the products. As for the remove function, I decided to simply warn the user that if the quantity of product is 3, then all 3 products will be removed from cart.

Okay, now when all crucial parts are implemented, we can now send the order to the n8n and then the automation can begin.

When sending the order I forgot to add customer ID, because that also is stored inside the database. To achieve this I had to change few things.
- When user is authenticating, I also had to return the ID of the user which I was not doing.
- Then instead of passing only the user type to the `menu.py`, I pass the entire user to it and then parse the user type inside that file.
- And then when user is happy with the cart and wants to confirm the order, I additionally to the cart I pass the user to the `webhook.py` so I can add the user ID to the payload which will be stored inside the database.

And while I am here, I might as well add total price to payload.