# Feature file for home page of Telvero.
Feature: Telvero home page functionality


  # Preconditions for the user.
  Background:
    Given the user is not logged in on the Telvero site
    * user is on Telvero home page


  @positive @login @navbar
  Scenario: A user can navigate to login as Telvero user
    Given the user navigates to the navbar 'Login' button
    When the user clicks on the 'Login' button
    Then the login page launches


  # Add in all navbar givens the color changing to light green background color (hovering).
  @positive @navbar
  Scenario: A user can navigate to learn why to use Telvero
    Given the user navigates to the navbar 'Why Telvero' button
    When the user clicks on the 'Why Telvero' button
    Then the why-telvero page launches


  @positive @navbar
  Scenario: A user can navigate to learn how Telvero works
    Given the user navigates to the navbar 'How it Works' button
    When the user clicks on the 'How it Works' button
    Then the how-it-works page launches


  @positive @navbar
  Scenario: A user can navigate to learn more about the features of Telvero
    Given the user navigates to the navbar 'Features' button
    When the user clicks on the 'Features' button
    Then the features page launches


  @positive @navbar
  Scenario: A user can navigate to learn about the pricing of Telvero
    Given the user navigates to the navbar 'Why Telvero' button
    When the user clicks on the 'Why Telvero' button
    Then the pricing page launches


  @positive @register @navbar
  Scenario: A user can navigate to register as a new customer
    Given the user navigates to the navbar 'Try It For Free' button
    When the user clicks on the 'Try It For Free' header button
    Then the registration page launches


  # //a/*[contains(text(), 'Try It Free')] for 'Why Telvero' and 'Features' tabs.
  # //a/*[contains(text(), 'Try It For Free')] for 'How it Works' and 'Pricing' tabs.
  @positive @register @wip
  Scenario: A user can navigate in page to register as a new customer
    Given the user navigates to the 'Try It For Free' button
    When the user clicks on the 'Try It For Free' page button
    Then the registration page launches
