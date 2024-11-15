from flasgger import Swagger

# Swagger configuration
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "specs": [
                {
                    "endpoint": 'login',
                    "route": '/login',
                    "spec": '/swagger/login.yaml'
                },
                {
                    "endpoint": 'register',
                    "route": '/register',
                    "spec": '/swagger/register.yaml'
                },
                {
                    "endpoint": 'github_stats',
                    "route": '/api/github/stats',
                    "spec": '/swagger/github_stats.yaml'
                }
            ],
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs"
}

template = {
    "info": {
        "title": "GitHub Stats API Gateway",
        "description": "API Gateway for managing GitHub statistics and user authentication",
        "version": "1.0.0",
        "contact": {
            "name": "KEA",
            "url": "https://kea.dk"
        }
    },
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "JWT Authorization header using the Bearer scheme. Example: \"Bearer {token}\""
        }
    }
}

def init_swagger(app):
    """Initialize Swagger with the given Flask app"""
    return Swagger(app, config=swagger_config, template=template)