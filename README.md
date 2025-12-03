# 🛒 Grocery Store Manager

A beautiful and responsive web application for managing grocery store inventory and generating customer bills, built with Streamlit.

## ✨ Features

- **📊 Rate List**: View all products and their prices in an organized table format
- **💰 Bill Generation**: Create customer bills with an interactive shopping cart
- **➕ Add Items**: Add new products to existing categories or create new categories
- **🗑️ Remove Items**: Remove products or entire categories from inventory
- **📱 Fully Responsive**: Works seamlessly on desktop, tablet, and mobile devices
- **🎨 Animated UI**: Smooth animations and transitions for better user experience
- **💾 Session Management**: Cart and inventory persist during your session

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/grocery-store-manager.git
cd grocery-store-manager
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

4. Open your browser and navigate to:
```
http://localhost:8501
```

## 📖 Usage

### Home Page
- View total categories, products, and cart items
- Browse current inventory by category

### Generate Bill
1. Enter customer name
2. Select category and item
3. Choose size/price option
4. Enter quantity
5. Add to cart
6. Generate bill when ready

### Rate List
- View all products with their prices in a clean table format
- Organized by categories

### Add Items
- **Add to Existing Category**: Add new products to current categories
- **Create New Category**: Create a new category with its first product

### Remove Items
- **Remove Item**: Delete specific products from categories
- **Remove Category**: Delete entire categories (with warning)

## 🎨 Features Highlights

- **Gradient Headers**: Beautiful gradient backgrounds
- **Hover Effects**: Cards lift on hover for better interactivity
- **Smooth Animations**: Fade-in and slide-in effects
- **Color-Coded Actions**: Different colors for different action types
- **Responsive Layout**: Adapts to any screen size
- **Real-time Updates**: Instant feedback on all actions

## 📁 Project Structure

```
grocery-store-manager/
│
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
└── display.py         # Original CLI version (legacy)
```

## 🛠️ Technologies Used

- **Streamlit**: Web framework for data apps
- **Python**: Core programming language
- **CSS**: Custom styling and animations
- **HTML**: Custom components

## 🌐 Deployment

### Deploy to Streamlit Cloud

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Click "New app"
5. Select your repository, branch, and `app.py`
6. Click "Deploy"

### Deploy to Heroku

1. Create a `Procfile`:
```
web: streamlit run app.py --server.port=$PORT
```

2. Deploy:
```bash
heroku create your-app-name
git push heroku main
```

### Deploy to Other Platforms

The app can be deployed to any platform that supports Python web applications:
- Railway
- Render
- PythonAnywhere
- AWS/GCP/Azure

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

Your Name
- GitHub: [@yourusername](https://github.com/yourusername)

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Icons from emoji
- Inspired by modern e-commerce interfaces

## 📸 Screenshots

### Home Page
Dashboard showing inventory overview with metrics and expandable categories.

### Bill Generation
Interactive shopping cart with real-time total calculation and smooth animations.

### Rate List
Clean table view of all products organized by category.

### Add/Remove Items
Easy-to-use forms for managing inventory with instant feedback.

---

Made with ❤️ using Streamlit
