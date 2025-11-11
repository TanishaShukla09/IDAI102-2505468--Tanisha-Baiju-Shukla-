# IDAI102-2505468--Tanisha-Baiju-Shukla-
# MedTimer - Daily Medicine Companion

## Project Overview

MedTimer is a medicine tracking application designed for elderly users and individuals managing chronic conditions. Built with Python and Streamlit, this application helps users manage their daily medication routines effectively.

### Purpose

MedTimer helps users:
- Track daily medications
- Set reminders for medicine schedules
- Monitor medication adherence
- Maintain records for healthcare providers
- Manage multiple medications easily

### Target Audience

- Elderly adults managing multiple medications
- Individuals with chronic conditions
- Caregivers supporting family members
- Anyone needing medication tracking

## Key Features

## Key Features

### Core Features

1. **Location-Aware Medicine Database**
   - Supports 12+ countries with region-specific medications
   - Pre-populated medicine lists for common chronic conditions
   - Automatic timezone detection based on location

2. **Medicine Management**
   - Add, edit, and delete medicines
   - Set custom reminder times for each medication
   - Support for multiple medications per day

3. **Visual Status Tracking**
   - Green: Medicine taken
   - Red: Medicine missed
   - Yellow: Medicine due now
   - Gray: Upcoming scheduled dose

4. **Guided Setup Wizard**
   - Step-by-step onboarding process
   - Easy interface for all users
   - Six-step setup process

5. **Quick Add Mode**
   - Advanced mode for experienced users
   - Rapid medicine entry
   - Comprehensive statistics dashboard

6. **Adherence Tracking**
   - Real-time statistics
   - Visual progress indicators
   - Color-coded medication cards

7. **Multiple Themes**
   - 5 themes available: Sage Garden, Ocean Breeze, Sunset Warmth, Lavender Dreams, Spring Blossom
   - Custom color palettes
   - Adjustable text size (18px - 24px)

8. **Data Backup and Restore**
   - Download medication data as JSON
   - Upload previously saved data
   - Prescription file upload support

## Technology Stack

- Python 3.8+
- Streamlit - Web application framework
- Pandas - Data manipulation
- JSON - Data storage
- Datetime - Time-based tracking
- Custom CSS - UI styling

## Prerequisites

- Python 3.8 or higher
- pip package manager
- Internet connection

## Installation and Setup

## Installation and Setup

### Local Installation Steps

1. Install required packages
```bash
pip install -r requirements.txt
```

2. Run the application
```bash
streamlit run app.py
```

3. Open browser at http://localhost:8501

### Requirements File

Create a file named requirements.txt with:
```
streamlit
pandas
```

## Deployment

### Streamlit Cloud Deployment Steps

1. Create GitHub repository with code
2. Add app.py and requirements.txt
3. Go to https://streamlit.io/
4. Click Deploy an app
5. Connect GitHub account
6. Select repository
7. Deploy

Live App URL: https://medtimer.streamlit.app/

## How to Use

## How to Use

### Guided Setup Mode

Step 1: Enter your name

Step 2: Select location (country and region)

Step 3: Choose chronic condition

Step 4: Review and edit medicines
- Pre-loaded medicines appear
- Edit names as needed
- Add custom medicines
- Delete unwanted entries

Step 5: Set medicine times for each medication

Step 6: Access dashboard
- View daily schedule
- Mark medicines as taken
- Upload prescriptions
- Download/restore data

### Quick Add Mode

1. Select country, region, and condition
2. Choose medicine from dropdown
3. Set reminder time
4. Add notes (optional)
5. Click Add Medicine
6. Manage medicines in dashboard

## User Interface Design

### Design Principles

1. Accessibility
   - Large fonts (18px - 24px)
   - High contrast colors
   - Clear visual hierarchy
   - Simple navigation

2. Visual Design
   - Soft color palettes
   - Gradient backgrounds
   - Card-based layout
   - Responsive design

3. User Feedback
   - Color-coded status
   - Animated buttons
   - Success messages
   - Visual confirmations

### Available Themes

- Sage Garden: Green and beige tones
- Ocean Breeze: Blue color scheme
- Sunset Warmth: Orange and yellow colors
- Lavender Dreams: Purple shades
- Spring Blossom: Pink tones

## Data Management

### Data Storage Format

Medicine data is stored in JSON format:

```json
{
  "profile": {
    "name": "John Doe",
    "country": "India",
    "timezone": "Asia/Kolkata",
    "disease": "Hypertension"
  },
  "meds": [
    {
      "name": "Amlodipine 5mg",
      "time": "08:00"
    }
  ],
  "med_status": {
    "Amlodipine 5mg": "taken"
  }
}
```

### Backup and Restore Features

- Download all data as JSON file
- Upload previously saved data
- Prescription file uploads (PDF, JPG, PNG)

## Supported Countries and Conditions

### Countries Supported
India, United States, United Kingdom, Australia, Canada, Germany, France, Japan, China, Brazil, Spain, Italy

### Chronic Conditions
- Hypertension
- Diabetes Type 2
- Hypothyroidism
- Asthma
- COPD
- Heart Disease
- Arthritis
- Depression
- Anxiety
- Migraine

Each condition includes country-specific pre-loaded medications.

## Testing

## Testing

### Test Scenarios

1. User Flow Testing
   - Complete guided setup process
   - Quick add medicine functionality
   - Medicine status updates

2. Edge Cases
   - Multiple medicines at same time
   - Medicine scheduling across different times
   - Empty medicine lists

3. Device Testing
   - Desktop browsers
   - Tablet devices
   - Mobile phones

## Design Decisions

### Key Design Choices

1. Guided wizard reduces complexity for elderly users
2. Color coding provides clear visual feedback
3. Large fonts improve readability
4. Minimal clicks reduce user frustration
5. Simple interface follows common UI patterns

### Accessibility Features

- High color contrast
- Large button sizes (minimum 48px)
- Clear text labels
- Responsive layouts

## Known Limitations

- No system-level push notifications
- Session-based storage (use backup feature)
- Single user per session
- Shows current day status only

## Future Improvements

- Push notifications for reminders
- Cloud database integration
- Multi-day calendar view
- Family member access
- Weekly and monthly reports
- Voice-activated logging

## Code Structure

### Main Components

1. Configuration
   - Theme definitions
   - Country and disease databases
   - CSS styling

2. Data Functions
   - load_data(): Loads medicine data from JSON
   - save_data(): Saves medicine data to JSON
   - get_med_status(): Determines medicine status based on time

3. Session State Management
   - User profile data
   - Medicine list
   - Medicine status tracking
   - Step tracking for guided mode

4. User Interface
   - Sidebar with settings
   - Guided setup mode (6 steps)
   - Quick add mode
   - Dashboard with medicine cards

### Key Python Concepts Used

- Lists and Dictionaries for data storage
- Datetime module for time-based tracking
- JSON for data persistence
- Streamlit for web interface
- Session state for user data
- Conditional logic for medicine status
- File handling for backup/restore

## Screenshots

### Main Dashboard
[Add screenshot of dashboard]

### Guided Setup
[Add screenshot of setup process]

### Quick Add Mode
[Add screenshot of quick add interface]

### Theme Options
[Add screenshot showing different themes]

### Completed Stages

Stage 1: Problem understanding and design planning - Completed
Stage 2: Python logic implementation - Completed
Stage 3: Interactive Streamlit interface - Completed
Stage 4: Testing and creative features - Completed
Stage 5: Deployment and documentation - Completed

### Features Implemented

All compulsory features have been implemented:
- Medicine input and management
- Visual checklist with color coding
- Time-based status updates
- Adherence tracking
- Motivational elements
- Data backup and restore

## References

- Streamlit Documentation: https://docs.streamlit.io/
- Python Datetime Module: https://docs.python.org/3/library/datetime.html
- UX Design for Seniors: https://www.eleken.co/blog-posts/examples-of-ux-design-for-seniors

## License

This project is created as part of academic coursework for Python Programming course.
