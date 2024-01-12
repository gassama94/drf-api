# Catch-up API: Manual Testing Documentation

## Overview

Catch-up API serves as a robust digital platform designed for an interactive blogging community. It offers a comprehensive suite of features for blog post management, social interactions through comments, likes, and followers, and user profile customization. The API is tailored for content sharing and social engagement, making it ideal for a dynamic blogging application.

## Features

### Blog Posts Management
- **Create, View, Edit, and Delete Posts:** Users can actively manage their blog posts, fostering a community of content creators and readers.

### Comments System
- **Engage in Discussions:** Users can comment on blog posts, enhancing platform interactivity.

### Likes and Followers
- **Social Networking:** Enables users to like posts and follow other users, adding a social dimension.

### Profile Management
- **Personalization:** Users can create and edit their profiles to add a personal touch to their interactions.

### Categories System
- **Organized Navigation:** Posts are categorized for easier discovery and structured browsing.

## Security and Accessibility

### User Authentication
- **Secure Interaction:** Only authenticated users can create and interact with content, ensuring a personalized experience.

### Administrator Controls
- **Content Moderation:** Administrators have special privileges for maintaining content quality and appropriateness.

## Intended Use
Catch-up API is designed for a blogging application focused on content creation, sharing, and community interaction, aiming to provide an intuitive and engaging user experience.

## Methodology for Manual Testing

### Approach
- **Inserting New Data:** Evaluated each endpoint by inserting legitimate and invalid data, observing the response and error handling.
- **User Authentication Testing:** Confirmed that only authenticated users have permissions to create and interact with posts and profiles.
- **Administrator Functions:** Tested admin capabilities for deleting inappropriate content.

### Profiles Endpoint
- **PUT Method Testing:** Verified that only the profile's owner can update specific details.

### Posts Endpoint
- **Authenticated vs Unauthenticated Access:** Ensured correct permissions for viewing, creating, and interacting with posts.
- **Image Size Limitation:** Confirmed the functionality of uploading posts with size-limited images.

### Comments Endpoint
- **View vs Post Permissions:** Checked that logged-out users can only view comments, while logged-in users can post, edit, and delete.

### Likes Endpoint
- **Adding and Removing Likes:** Tested the functionality for authenticated users to like and 'unlike' posts.

### Followers Endpoint
- **Follow/Unfollow Functionality:** Ensured that logged-in users can follow and unfollow others and view followers list.

### Categories Endpoint
- **Post Categorization:** Confirmed the ability of users to categorize their posts.

## Conclusion

### Summary of Findings
- **Effective User Authentication and Access Control**
- **Seamless Content Management**
- **Robust Social Interactions**
- **Customizable User Profiles**
- **Efficient Content Categorization**
- **Effective Administrator Controls**

### Recommendations for Improvement
1. **Improved Error Handling**
2. **Enhanced Search Functionality**
3. **Performance Optimization**
4. **User Interface Enhancements**
5. **Additional Social Features**
6. **Accessibility Improvements**
7. **Regular Updates Based on User Feedback**

In conclusion, the Catch-up API exhibits robust capabilities for a blogging community platform, with potential for further enhancements based on user feedback and technological advancements.