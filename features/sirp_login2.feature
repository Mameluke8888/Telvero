# Feature file for login page of Telvero (app.telvero.com).
Feature: Telvero login page functionality


  # Preconditions for user.
  Background:
    Given the user is not logged in on the Telvero site
    * user is on Telvero login page


  @positive @attempt @skip
  Scenario: A user can sign in using correct email and password
    Given the user enters their email and password
    When the user clicks the 'Sign In' button
    Then the user's profile page launches


  @negative @attempt
  Scenario: A user can't sign in using incorrect email and/or password
    Given the user enters incorrect email and password
    When the user clicks the 'Sign In' button
    Then red error pop up says 'The credentials you provided appear to be invalid. Try again?'


  @negative @attempt
  Scenario: A user can't sign in using empty email and password
    Given the user has email and password fields empty
    When the user clicks the 'Sign In' button
    Then below both fields a pop up says 'Email shouldn't be empty' and 'Password shouldn't be empty'


  # Less than 8 characterse long.
  @negative @attempt
  Scenario: A user can't sign in using short password
    Given the user enters their email and a short password
    When the user clicks the 'Sign In' button
    Then error below password field pops up saying 'the password is too short'


  @positive @register
  Scenario: A user can navigate to create an account
    Given the user navigates to the 'Create Account' button
    When the user clicks on the 'Create Account' button
    Then the registration page launches


  @positive @wip
  Scenario: A user can navigate to forget password option
    Given the user navigates to the 'Forget a password?' button
    When the user clicks on the 'Forget a password?' button
    Then the reset_password page launches

