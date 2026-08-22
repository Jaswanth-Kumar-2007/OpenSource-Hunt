const OWNER = "Jaswanth-Kumar-2007";
const REPO = "OpenSource-Hunt";

const API_URL = `https://api.github.com/repos/${OWNER}/${REPO}`;

const prContainer = document.getElementById("pr-container");
const loading = document.getElementById("loading");
const errorBox = document.getElementById("error");
const prCount = document.getElementById("pr-count");

let pullRequests = [];
let currentFilter = "all";


// -------------------------------------
// Fetch Pull Requests
// -------------------------------------

async function fetchPullRequests() {

    try {

        const response = await fetch(
            `${API_URL}/pulls?state=all&sort=created&direction=desc&per_page=100`
        );

        if (!response.ok) {
            throw new Error("Failed to fetch pull requests.");
        }

        pullRequests = await response.json();

        loading.classList.add("hidden");

        updateCount();

        displayPullRequests();

    } catch (error) {

        loading.classList.add("hidden");

        errorBox.textContent = error.message;

        errorBox.classList.remove("hidden");
    }
}


// -------------------------------------
// Fetch commits for one PR
// -------------------------------------

async function fetchCommits(prNumber) {

    try {

        const response = await fetch(
            `${API_URL}/pulls/${prNumber}/commits?per_page=100`
        );

        if (!response.ok) {
            throw new Error("Failed to fetch commits.");
        }

        return await response.json();

    } catch (error) {

        console.error(error);

        return [];

    }
}


// -------------------------------------
// Display Pull Requests
// -------------------------------------

async function displayPullRequests() {

    prContainer.innerHTML = "";

    let filteredPRs = pullRequests;

    if (currentFilter !== "all") {

        filteredPRs = pullRequests.filter(
            pr => pr.state === currentFilter
        );

    }


    if (filteredPRs.length === 0) {

        prContainer.innerHTML = `
            <div class="no-pr">
                <h3>No Pull Requests Found</h3>
                <p>
                    There are no ${currentFilter === "all"
                        ? ""
                        : currentFilter
                    } pull requests.
                </p>
            </div>
        `;

        return;
    }


    for (const pr of filteredPRs) {

        const card = createPRCard(pr);

        prContainer.appendChild(card);

        loadCommits(pr, card);
    }
}


// -------------------------------------
// Create PR Card
// -------------------------------------

function createPRCard(pr) {

    const card = document.createElement("article");

    card.className = "pr-card";

    const statusClass =
        pr.state === "open"
            ? "open"
            : "closed";


    const statusText =
        pr.state === "open"
            ? "● Open"
            : "● Closed";


    const mergedText =
        pr.merged_at
            ? " • Merged"
            : "";


    card.innerHTML = `

        <div class="pr-header">

            <div class="pr-title-row">

                <div>

                    <a
                        class="pr-title"
                        href="${pr.html_url}"
                        target="_blank"
                    >
                        ${escapeHTML(pr.title)}
                    </a>

                    <span class="pr-number">
                        #${pr.number}
                    </span>

                </div>

                <span class="status ${statusClass}">
                    ${statusText}
                </span>

            </div>


            <div class="pr-info">

                <img
                    class="avatar"
                    src="${pr.user.avatar_url}"
                    alt="${pr.user.login}"
                >

                <span>
                    ${escapeHTML(pr.user.login)}
                </span>

                <span>•</span>

                <span>
                    ${formatDate(pr.created_at)}
                </span>

                <span>
                    ${mergedText}
                </span>

            </div>

        </div>


        <div class="pr-body">

            <h3 class="commit-heading">
                Commits
                <span class="commit-count">Loading...</span>
            </h3>

            <div class="commits">
                <p>Loading commits...</p>
            </div>

        </div>
    `;

    return card;
}


// -------------------------------------
// Load commits into PR card
// -------------------------------------

async function loadCommits(pr, card) {

    const commitsContainer =
        card.querySelector(".commits");

    const commitCount =
        card.querySelector(".commit-count");


    const commits = await fetchCommits(pr.number);


    commitCount.textContent =
        `(${commits.length})`;


    if (commits.length === 0) {

        commitsContainer.innerHTML = `
            <p>
                No commits found.
            </p>
        `;

        return;
    }


    commitsContainer.innerHTML = "";


    commits.forEach(commit => {

        const commitElement =
            document.createElement("div");

        commitElement.className = "commit";


        const shortSha =
            commit.sha.substring(0, 7);


        const message =
            commit.commit.message.split("\n")[0];


        const author =
            commit.author?.login ||
            commit.commit.author?.name ||
            "Unknown";


        const date =
            commit.commit.author?.date;


        commitElement.innerHTML = `

            <div class="commit-icon">
                🔹
            </div>

            <div class="commit-content">

                <a
                    class="commit-message"
                    href="${commit.html_url}"
                    target="_blank"
                >
                    ${escapeHTML(message)}
                </a>

                <div class="commit-meta">

                    <span>
                        ${escapeHTML(author)}
                    </span>

                    <span> • </span>

                    <span>
                        ${formatDate(date)}
                    </span>

                    <span> • </span>

                    <span class="sha">
                        ${shortSha}
                    </span>

                </div>

            </div>
        `;


        commitsContainer.appendChild(commitElement);

    });
}


// -------------------------------------
// Update PR count
// -------------------------------------

function updateCount() {

    const openCount =
        pullRequests.filter(
            pr => pr.state === "open"
        ).length;


    const closedCount =
        pullRequests.filter(
            pr => pr.state === "closed"
        ).length;


    prCount.textContent =
        `${pullRequests.length} total • ${openCount} open • ${closedCount} closed`;
}


// -------------------------------------
// Filter buttons
// -------------------------------------

document
    .querySelectorAll(".filter-btn")
    .forEach(button => {

        button.addEventListener("click", () => {

            document
                .querySelectorAll(".filter-btn")
                .forEach(btn => {
                    btn.classList.remove("active");
                });


            button.classList.add("active");


            currentFilter =
                button.dataset.filter;


            displayPullRequests();

        });

    });


// -------------------------------------
// Format date
// -------------------------------------

function formatDate(date) {

    if (!date) {
        return "Unknown date";
    }

    return new Date(date).toLocaleDateString(
        "en-IN",
        {
            day: "numeric",
            month: "short",
            year: "numeric"
        }
    );
}


// -------------------------------------
// Prevent HTML injection
// -------------------------------------

function escapeHTML(value) {

    if (!value) {
        return "";
    }

    return String(value)
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");
}


// Start
fetchPullRequests();