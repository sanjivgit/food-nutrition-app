# 🥗 Food Nutrition App

A modern, AI-powered FastAPI application designed to help users analyze and track nutritional information from food items. This application provides detailed insights into calories, macronutrients, and micronutrients through an intelligent backend API.

## 📋 Table of Contents

- [About](#about)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [API Documentation](#api-documentation)
- [Development](#development)
- [Contributing](#contributing)

## 🎯 About

The Food Nutrition App is a comprehensive solution for nutritional data analysis. It leverages modern Python technologies to deliver fast, reliable, and accurate nutritional information for food items. Whether you're building a fitness tracking application, a dietary management system, or conducting nutritional research, this API provides the backbone you need.

### What It Does

- **Nutritional Analysis**: Analyze any food item and get comprehensive nutritional breakdowns
- **Macro & Micronutrient Tracking**: Monitor proteins, carbs, fats, vitamins, and minerals
- **AI-Powered Insights**: Leverage AI capabilities for intelligent food recommendations
- **RESTful API**: Easy-to-integrate endpoints for seamless integration
- **Scalable Architecture**: Built for performance and reliability

### How It Works

1. **Accept Food Input**: Users submit food items or meal descriptions
2. **Data Processing**: The system processes the input through intelligent algorithms
3. **Nutritional Analysis**: Comprehensive nutritional data is calculated
4. **Return Results**: Detailed JSON responses with complete nutritional information
5. **Track History**: All data can be stored and analyzed over time

## ✨ Key Features

### Core Functionality
- 🍎 **Food Database Integration**: Access to comprehensive food nutrition database
- 📊 **Detailed Analytics**: Complete breakdown of macronutrients and micronutrients
- 🤖 **AI-Enhanced Processing**: Smart food recognition and analysis
- ⚡ **High Performance**: Optimized for speed and efficiency
- 🔄 **RESTful API Design**: Clean, intuitive endpoints

### Developer Features
- 📚 **Auto-Generated API Docs**: Interactive Swagger UI and ReDoc documentation
- 🐳 **Docker Support**: Easy containerization and deployment
- 🔌 **Modular Architecture**: Organized code structure for easy maintenance
- ✅ **Production Ready**: Error handling and validation built-in
- 📝 **Comprehensive Logging**: Detailed logging for debugging

## 🛠️ Tech Stack

### Backend Framework
- **FastAPI**: Modern, fast (high-performance) web framework for building APIs
- **Python 3.10**: Reliable and powerful programming language
- **Uvicorn**: Lightning-fast ASGI server

### Infrastructure
- **Docker & Docker Compose**: Containerization for consistent environments
- **Python Virtual Environment**: Isolated dependency management

### Architecture Highlights
- Modular service-based architecture
- RESTful API design patterns
- Scalable configuration management
- Professional error handling

## 📁 Project Structure
/api/v1/
├── /nutrition/    # Nutrition analysis endpoints
├── /foods/        # Food database endpoints
├── /meals/        # Meal planning endpoints
└── /health/       # Health check endpoints


### Directory Details

- **`src/app/main.py`**: Entry point for the FastAPI application, router initialization
- **`src/app/config.py`**: Centralized configuration management
- **`src/app/api/v1/`**: API v1 endpoints and route handlers
- **`src/app/models/`**: Pydantic models for request/response validation
- **`src/app/services/`**: Business logic and service layer implementation
- **`src/app/core/`**: Core utilities, dependencies, and middleware

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher
- Docker and Docker Compose (optional)
- Git

### Installation

#### Option 1: Using Docker (Recommended)

# Navigate to server directory
cd server

# Build and run with Docker Compose
docker-compose up --build

Application will be available at http://localhost:8000

#### Option 2: Local Development

#### Navigate to server directory
cd server

#### Create virtual environment
python -m venv venv

#### Activate virtual environment
#### On Windows:
venv\Scripts\activate
#### On macOS/Linux:
source venv/bin/activate

#### Install dependencies
pip install -r requirements.txt

# Run the application
python -m uvicorn src.app.main:app --host 0.0.0.0 --port 8000 --reload
