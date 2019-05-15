Feature: test search filed
  As a User
  That can span a few lines

  Scenario: Homepage can go to Contact
    Given I am on the homepage
    When I click on the link with id "blog-link"
    #Then I am on the blog page
