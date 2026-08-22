const OWNER = "Jaswanth-Kumar-2007";
const REPO = "OpenSource-Hunt";

const API_URL =
    `https://api.github.com/repos/${OWNER}/${REPO}`;


const prContainer =
    document.getElementById("pr-container");

const loading =
    document.getElementById("loading");

const errorBox =
    document.getElementById("error");

const prCount =
    document.getElementById("pr-count");

const leaderboard =
    document.getElementById("leaderboard");


let pullRequests = [];

let currentFilter = "all";


// ======================================================
// FETCH ALL PULL REQUESTS
// ======================================================

async function fetchAllPullRequests() {

    let allPRs = [];

    let page = 1;

    const perPage = 100;


    while (true) {

        const response = await fetch(
            `${API_URL}/pulls?state=all&sort=created&direction=desc&per_page=${perPage}&page=${page}`
        );


        if (!response.ok) {

            throw new Error(
                "Failed to fetch pull requests."
            );

        }


        const prs = await response.json();


        allPRs.push(...prs);


        // If less than 100 were returned,
        // there are no more pages.

        if (prs.length < perPage) {
            break;
        }


        page++;

    }


    return allPRs;
}


// ======================================================
// FETCH ALL COMMITS OF A PR
// ======================================================

async function fetchAllCommits(prNumber) {

    let allCommits = [];

    let page = 1;

    const perPage = 100;


    while (true) {

        const response = await fetch(
            `${API_URL}/pulls/${prNumber}/commits?per_page=${perPage}&page=${page}`
        );


        if (!response.ok) {

            console.error(
                `Failed to fetch commits for PR #${prNumber}`
            );

            break;
        }


        const commits = await response.json();


        allCommits.push(...commits);


        if (commits.length < perPage) {
            break;
        }


        page++;

    }


    return allCommits;
}


// ======================================================
// MAIN FETCH
// ======================================================

async function loadData() {

    try {

        loading.classList.remove("hidden");


        pullRequests =
            await fetchAllPullRequests();


        console.log(
            `Loaded ${pullRequests.length} PRs`
        );


        loading.classList.add("hidden");


        updateCount();


        displayPullRequests();


        await generateLeaderboard();


    } catch (error) {

        loading.classList.add("hidden");

        errorBox.textContent =
            error.message;

        errorBox.classList.remove("hidden");

    }

}


// ======================================================
// DISPLAY PULL REQUESTS
// ======================================================

async function displayPullRequests() {

    prContainer.innerHTML = "";


    let filteredPRs =
        pullRequests;


    if (currentFilter !== "all") {

        filteredPRs =
            pullRequests.filter(
                pr => pr.state === currentFilter
            );

    }


    if (filteredPRs.length === 0) {

        prContainer.innerHTML = `

            <div class="no-pr">

                <h3>
                    No Pull Requests Found
                </h3>

                <p>
                    There are no
                    ${currentFilter === "all"
                        ? ""
                        : currentFilter
                    }
                    pull requests.
                </p>

            </div>

        `;

        return;

    }


    for (const pr of filteredPRs) {

        const card =
            createPRCard(pr);


        prContainer.appendChild(card);


        loadCommits(pr, card);

    }

}


// ======================================================
// CREATE PR CARD
// ======================================================

function createPRCard(pr) {

    const card =
        document.createElement("article");


    card.className =
        "pr-card";


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


                <span
                    class="status ${statusClass}"
                >
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

                <span class="commit-count">
                    Loading...
                </span>

            </h3>


            <div class="commits">

                <p>
                    Loading commits...
                </p>

            </div>

        </div>

    `;


    return card;

}


// ======================================================
// LOAD COMMITS FOR PR
// ======================================================

async function loadCommits(pr, card) {

    const commitsContainer =
        card.querySelector(".commits");


    const commitCount =
        card.querySelector(".commit-count");


    const commits =
        await fetchAllCommits(pr.number);


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


        commitElement.className =
            "commit";


        const shortSha =
            commit.sha.substring(0, 7);


        const message =
            commit.commit.message
                .split("\n")[0];


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


        commitsContainer.appendChild(
            commitElement
        );

    });

}


// ======================================================
// LEADERBOARD
// ======================================================

async function generateLeaderboard() {

    leaderboard.innerHTML = `

        <div class="loading">
            Calculating leaderboard...
        </div>

    `;


    const contributors = {};


    /*
        Go through every PR.
    */

    for (const pr of pullRequests) {

        const username =
            pr.user.login;


        /*
            Create contributor
            if they don't exist.
        */

        if (!contributors[username]) {

            contributors[username] = {

                username: username,

                avatar:
                    pr.user.avatar_url,

                profile:
                    pr.user.html_url,

                prs: 0,

                commits: 0

            };

        }


        /*
            Count PR.
        */

        contributors[username].prs++;


        /*
            Get commits of this PR.
        */

        const commits =
            await fetchAllCommits(
                pr.number
            );


        /*
            Add commits.
        */

        contributors[username].commits +=
            commits.length;

    }


    /*
        Convert object to array.
    */

    const leaderboardData =
        Object.values(contributors);


    /*
        SORTING RULE:

        1. More PRs first
        2. If same PRs,
           more commits first
        3. If still same,
           alphabetical username
    */

    leaderboardData.sort(
        (a, b) => {

            if (b.prs !== a.prs) {

                return b.prs - a.prs;

            }


            if (b.commits !== a.commits) {

                return b.commits - a.commits;

            }


            return a.username
                .localeCompare(
                    b.username
                );

        }
    );


    displayLeaderboard(
        leaderboardData
    );

}


// ======================================================
// DISPLAY LEADERBOARD
// ======================================================

function displayLeaderboard(data) {

    leaderboard.innerHTML = "";


    data.forEach(
        (user, index) => {

            const rank =
                index + 1;


            const card =
                document.createElement(
                    "div"
                );


            card.className =
                "leaderboard-card";


            let rankDisplay =
                `#${rank}`;


            if (rank === 1) {
                rankDisplay = "🥇";
            }

            else if (rank === 2) {
                rankDisplay = "🥈";
            }

            else if (rank === 3) {
                rankDisplay = "🥉";
            }


            card.innerHTML = `

                <div class="rank">
                    ${rankDisplay}
                </div>


                <div class="leader-user">

                    <img
                        class="leader-avatar"
                        src="${user.avatar}"
                        alt="${user.username}"
                    >


                    <a
                        class="username"
                        href="${user.profile}"
                        target="_blank"
                    >
                        ${escapeHTML(
                            user.username
                        )}
                    </a>

                </div>


                <div class="stats">

                    <div class="stat">

                        <span class="stat-number">
                            ${user.prs}
                        </span>

                        PRs

                    </div>


                    <div class="stat">

                        <span class="stat-number">
                            ${user.commits}
                        </span>

                        Commits

                    </div>

                </div>

            `;


            leaderboard.appendChild(
                card
            );

        }
    );

}


// ======================================================
// PR COUNT
// ======================================================

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
        `${pullRequests.length} total • ` +
        `${openCount} open • ` +
        `${closedCount} closed`;

}


// ======================================================
// FILTER
// ======================================================

document
    .querySelectorAll(".filter-btn")
    .forEach(button => {

        button.addEventListener(
            "click",
            () => {

                document
                    .querySelectorAll(
                        ".filter-btn"
                    )
                    .forEach(btn => {

                        btn.classList.remove(
                            "active"
                        );

                    });


                button.classList.add(
                    "active"
                );


                currentFilter =
                    button.dataset.filter;


                displayPullRequests();

            }
        );

    });


// ======================================================
// DATE
// ======================================================

function formatDate(date) {

    if (!date) {
        return "Unknown date";
    }


    return new Date(date)
        .toLocaleDateString(
            "en-IN",
            {
                day: "numeric",
                month: "short",
                year: "numeric"
            }
        );

}


// ======================================================
// SECURITY
// ======================================================

function escapeHTML(value) {

    if (!value) {
        return "";
    }


    return String(value)

        .replaceAll(
            "&",
            "&amp;"
        )

        .replaceAll(
            "<",
            "&lt;"
        )

        .replaceAll(
            ">",
            "&gt;"
        )

        .replaceAll(
            '"',
            "&quot;"
        )

        .replaceAll(
            "'",
            "&#039;"
        );

}


// ======================================================
// START
// ======================================================

loadData();