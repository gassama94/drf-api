# Hidden wonders API Manual Testing
### Overview of Hidden Wonders API

The Hidden Wonders API is a robust digital platform designed for an interactive blogging community. This API serves as the backbone of a dynamic web application where users can engage with a wide range of content through blog posts, comments, likes, and followers. It's tailored to offer both social interaction and informational content sharing.

## Key Features
- **Blog Posts Management:** Users can create, view, edit, and delete blog posts. This feature is central to the platform, fostering a vibrant community of content creators and readers.
- **Comments System:** The API supports a comments feature, enabling users to engage in discussions on blog posts, enhancing the interactivity of the platform.
- **Likes and Followers Functionality:** Users can like posts and follow other users, adding a social networking dimension to the platform.
- **Profile Management:** Users can create and edit their profiles, adding a personal touch to their interactions on the platform.
- **Categories System:** The API categorizes posts, allowing for easier navigation and a more organized content structure.

## Security and Accessibility
- **User Authentication:** The API enforces user authentication for creating and interacting with content, ensuring a secure and personalized experience.
- **Administrator Controls:** Special privileges are granted to administrators for content moderation, vital for maintaining the quality and appropriateness of the content.

## Intended Use
The Hidden Wonders API is intended for use in a blogging application where content creation, sharing, and community interaction are key components. It aims to provide an intuitive and engaging user experience, ensuring both content creators and readers find value and connectivity on the platform.

By combining these features, the Hidden Wonders API aims to create a comprehensive and engaging online community, connecting users through shared interests and interactive content.


### Methodology
The approach I adopted for manually evaluating each endpoint involved inserting new data into every legitimate endpoint to observe its reaction. Subsequently, I inputted invalid data to determine if it would trigger appropriate error messages and codes. These evaluations were conducted using the Django Rest Framework HTML interface.

The API's primary function is to permit only authenticated users to create blog posts and to interact with these posts through likes, follows, and comments. Conversely, unauthenticated users are limited to merely viewing these posts, without the capability to interact in any manner. Access to this content is possible through the homepage, utilizing the search bar, or by navigating the categories dropdown menu. This design ensures that all visitors can peruse the site's content, even without a user profile, but they are restricted from creating posts or engaging with existing ones.

Thus, the functionality is such that only users who are logged in can create, modify, or remove posts, comments, likes, and followers. Additionally, authenticated users have the privilege to update their profiles, including details like username, password, biography, and profile picture. For an unauthenticated user, these functionalities should be inaccessible, which was a focus of my testing.

Furthermore, I integrated a feature that allows me, as an administrator, to delete posts and comments. This was implemented to eliminate any potential inappropriate or offensive content that might be uploaded to the site in the form of posts or comments. This aspect was also scrutinized during the testing phase.

### Profiles Endpoint
- api/profiles/
     - Test Scenarios.

     Regarding the endpoint for user profile details, it's designed so that only the profile's owner can modify specific details, like their username. In the accompanying image, you'll see how I conducted a test using the PUT method by inputting extra data into the content field. This was to ensure that the update functionality is restricted to the profile owner only.

     ![profiles](testing-images/profiles-logged-in.png)

  ### api/profiles/id/
     - Test Scenarios and Expected Results.

     This worked as intended.
     When I attempt to enter an invalid ID, I am shown a 404 error with the message Not Found. This can be seen below.

     ![profiles](testing-images/profiles-logged-out.png)

### Posts Endpoints
- api/posts/
     - Test Scenarios 
    
    - when user is logged out.
     ![posts](testing-images/postlist-logged-out.png)

    - when user is logged in 
     ![profiles](testing-images/postlist-logged-in.png)

   - api/posts/id/
     - Test Scenarios and Expected Results
     This worked as intended.
     When I attempt to enter an images that was more then 2MB, it didnt work, and i succesfully created a post with the crrecr size images. This can be seen below.

   - created a post 
     ![posts](testing-images/postlist-add-post.png)
   - images size too big 
     ![posts](testing-images/postlist-bigimage.png)

   - api/postsdetails/id/
   - updated a post 
     ![posts](testing-images/postdeatail-updated.png)

   - deleted post 
     ![posts](testing-images/postdetail-delete.png)


### Comments Endpoints
- api/comments/
     - Test Scenarions.
     When a user is logged out, they should only be able to view the comment list with this endpoint without the option of posting a comment. The image below shows the GET method working as intended.
     ![comments](testing-images/comment-loggedout.png)


     If a user is authenticated and logged in, however, they should have the added ability to both edit AND delete a comment only if they select the id of a comment that they posted. The image below displays these available options, as well as my attempt to update the current comment to test that the PUT request works as intended.
     ![comments](testing-images/commentlistdetail-png.png)

     The image below shows the PUT method working successfully with a 200 ok status code.
     ![comments](testing-images/commentlistdetail-png.png)
   - api/comments/id/
     - Expected Results
     The image below shows the comment being successfully posted with a 201 status code.
     ![comments](testing-images/commentsucess.png)

## Likes Endpoints
- api/likes/
     - Test Scenarios
     Users can like post
     ![likes](testing-images/Likeview.png)

     If a user is logged in and authenticated, however, they should have the option of adding a like on a particular post which can be accessed through a dropdown menu. This can be seen below.
     ![likes](testing-images/Likeedlist.png)

   - api/likes/id/
     - Test Scenarios and Expected Results
     This endpoint is for a specific like made by a user. If it's a logged-in user, they can also delete a like to represent them 'unliking' a blog post on the front end.
     ![likes](testing-images/LikeDelete.png)

     Users are unable to duplicate likes.
     ![likes](testing-images/likeduplicate.png)

     Logged out Users are unable to like a post.
     ![likes](testing-images/comment-loggedout.png)
  
### Followers Endpoints
- api/followers/
     - Test Scenarios
     A logged-in user should be able to both view the followers list as well as be able to follow other users authenticated on the site. This works as intended and can be seen below.
     ![followers](testing-images/Followerlist.png)
     A logged in user should be able to  follower other users.
     ![followers](testing-images/FollowedList.png.png)

     
   - api/followers/id/
     - Test Scenarios and Expected Results
     A logged-out user should be able to view a list of all followers and all instances of a user following another user. This works as intended and can be seen below.
     ![followers](testing-images/Followerloggedout.png)

     A logged-in individual,should also be able to delete a follower instance as you cannot edit it so that a user can stop following a profile. 
     ![followers](testing-images/followerdelete.png)


8. **Categories Endpoints**
   - api/category/
     - Test Scenarios and Expected Results

9. **Conclusion**
   - Summary of Findings
   - Recommendations for Improvement