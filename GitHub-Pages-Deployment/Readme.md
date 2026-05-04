# GitHub Pages Deployment Workflow

A foundational DevOps project demonstrating the implementation of **Continuous Integration and Continuous Deployment (CI/CD)** using **GitHub Actions**.

The core objective is to automate the deployment of a static environment to **GitHub Pages**, triggered specifically by changes to source files on the `main` branch.

## ⚙️ CI/CD Pipeline Logic
The workflow is defined in `.github/workflows/deploy.yml` and follows a strict trigger logic:
*   **Trigger:** Pushes to the `main` branch.
*   **Path Filter:** The workflow only executes if the `index.html` file is modified, preventing unnecessary builds.
*   **Environment:** Runs on `ubuntu-latest`.
*   **Deployment:** Utilizes official GitHub Action components to build and host the site on the GitHub Pages infrastructure.



## 🛠 Tech Stack
*   **Automation:** GitHub Actions
*   **Hosting:** GitHub Pages
*   **Language:** HTML5
*   **Version Control:** Git

## 📂 Project Structure
```text
gh-deployment-workflow/
├── .github/
│   └── workflows/
│       └── deploy.yml    # CI/CD Workflow definition
├── index.html            # Static entry point
└── README.md             # Project documentation
```

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/Seraph919/Roadmap-sh
cd Roadmap-sh/GitHub-Pages-Deployment
```

### 2. Implementation Details
The `deploy.yml` file utilizes the following permissions and steps:
*   `contents: read` and `pages: write` permissions.
*   **Checkout:** Pulls the latest code from the branch.
*   **Setup Pages:** Configures the runner for GitHub Pages deployment.
*   **Upload Artifact:** Bundles the `index.html` for deployment.
*   **Deploy:** Pushes the artifact to the live URL.

## 🌐 Live Demo
The live site is accessible at:
`https://Seraph919.github.io/Roadmap-sh/GitHub-Pages-Deployment`

## 🧠 Concepts Learned
*   **CI/CD Orchestration:** Automating the transition from code commit to production.
*   **Workflow Triggers:** Using `paths` filters to optimize runner usage.
*   **Artifact Management:** Storing and deploying build outputs within a pipeline.

---
**Author:** Ayoub Soudani  
**Part of the [DevOps Projects Lab](https://github.com/Seraph919/Roadmap-sh)**