<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
<h3 align="center">Simple API</h3>

  <p align="center">
    Visualisation of how to implement and deploy a simple API in both C# and Python
    <br />
    <a href="https://github.com/alaknas/SimpleAPI"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/alaknas/SimpleAPI">View Demo</a>
    ·
    <a href="https://github.com/alaknas/SimpleAPI/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/alaknas/SimpleAPI/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is a sample project, showcasing how to setup a simple API handler in both C# and Python, highlighting how two different languages can yield the same result.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* .NET C# (Using ASP.NET Core Web API)
* Python (Using FastAPI)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get started, clone this repo.

To start the C# version, open up the solution file in Visual Studio 2022 (Project is built using this IDE) and run it.

To start the Python version, launch it by entering the pyTaskManager folder and running:

```sh
uvicorn main:app --reload
```
or, if your uvicorn is not in the path:
```sh
python -m uvicorn main:app --reload
```

### Prerequisites

The solution itself is within the repo, and created with Visual Studio 2022.
The Python-version requires python3, pip, fastapi and uvicorn to be installed. 
Install fastapi and uvicorn with pip:

```sh
pip install fastapi uvicorn
```

The C# version requires Visual Studio 2022, and the .NET 9 libraries/runtimes.

<!-- USAGE EXAMPLES -->
## Usage

Either use a web-browser and point it to your localhost endpoint (visible in the output of either C# or Python version of the server), 
They are both able to handle:

* HTTP GET example: http://localhost:8000/Task/ -> gets you a list of any available tasks in the memory database.
* HTTP GET example: http://localhost:8000/Task/1 -> gets you task #1 (if available)
* HTTP GET example: http://localhost:8000/Task/summary -> gets you a summary of all tasks (if available)
* HTTP GET example: http://localhost:8000/Task/pending -> gets you a list of all tasks that are not completed (if available)
* HTTP PUT example: http://localhost:8000/Task/1 -> with a json body of title & description -> will modify task #1
* HTTP DELETE example: http://localhost:8000/Task/1 -> will remove task #1 if available
* HTTP POST example: http://localhost:8000/Task/ -> with json body of title & description -> will create a new task in the memory DB

(You can use the accompanied postman file called `Showcase_API.postman_collection.json` import it into postman to use it.)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [X] C# Version
- [X] Python Version
- [X] README With basic instructions

See the [open issues](https://github.com/alaknas/SimpleAPI/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top contributors:

<a href="https://github.com/alaknas/SimpleAPI/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=alaknas/SimpleAPI" alt="contrib.rocks image" />
</a>


<!-- CONTACT -->
## Contact

Jan Sankala - [@jansankala](https://x.com/jansankala) - jan@sankala.eu

Project Link: [https://github.com/alaknas/SimpleAPI](https://github.com/alaknas/SimpleAPI)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/alaknas/SimpleAPI.svg?style=for-the-badge
[contributors-url]: https://github.com/alaknas/SimpleAPI/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/alaknas/SimpleAPI.svg?style=for-the-badge
[forks-url]: https://github.com/alaknas/SimpleAPI/network/members
[stars-shield]: https://img.shields.io/github/stars/alaknas/SimpleAPI.svg?style=for-the-badge
[stars-url]: https://github.com/alaknas/SimpleAPI/stargazers
[issues-shield]: https://img.shields.io/github/issues/alaknas/SimpleAPI.svg?style=for-the-badge
[issues-url]: https://github.com/alaknas/SimpleAPI/issues
[license-shield]: https://img.shields.io/github/license/alaknas/SimpleAPI.svg?style=for-the-badge
[license-url]: https://github.com/alaknas/SimpleAPI/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/jan-sankala-2070855a
[product-screenshot]: images/screenshot.png
