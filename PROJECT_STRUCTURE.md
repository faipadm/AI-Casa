# AI-Casa

## Project Structure

AI-Casa/
├── backend/          # Contains backend services
│   ├── app/         # Main application logic
│   ├── config/      # Configuration files
│   ├── controllers/ # Business logic controllers
│   ├── models/      # Database models
│   ├── routes/      # API routes
│   ├── services/    # Services for business logic
│   ├── tests/       # Unit and integration tests for backend
│   └── server.js    # Entry point for the backend
│
├── frontend/        # Contains frontend services
│   ├── public/      # Public files (index.html, favicon, etc.)
│   ├── src/        # Source files for frontend
│   │   ├── components/  # React components
│   │   ├── pages/        # React pages
│   │   ├── App.js        # Main app file
│   │   └── index.js      # Entry point for the frontend
│   ├── package.json   # Frontend dependencies and scripts
│   └── README.md      # Frontend specific documentation
│
├── config/         # Project-wide configuration files
│   ├── .env         # Environment variables
│   ├── .gitignore    # Git ignore rules
│   ├── docker-compose.yml # Docker compose file
│   └── README.md     # General project structure documentation
│
├── scripts/         # Contains useful scripts
│   └── setup.sh      # Setup script to initialize environment
│
├── .github/         # GitHub related configurations
│   ├── workflows/    # GitHub Actions workflows
│   └── ISSUE_TEMPLATE.md # Issue templates
│
└── README.md        # Main project documentation
