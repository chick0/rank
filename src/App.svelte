<script>
    import { onMount } from "svelte";

    function fetch_rank_list() {
        fetch("/api/pull")
            .then((resp) => resp.json())
            .then((json) => {
                rank_list = json.list;
            })
            .catch(() => {
                alert("알 수 없는 오류가 발생했습니다!");
            });
    }

    /**
     * @typedef {Object} Rank
     * @property {number} id
     * @property {string} name
     * @property {number} score
     * @property {number} created_at
     */

    /** @type {Rank[]} */
    let rank_list = [];

    onMount(() => {
        fetch_rank_list();
        setInterval(() => {
            fetch_rank_list();
        }, 2500);
    });
</script>

<div class="section">
    <div class="container">
        <h1 class="title is-1 has-text-centered">랭킹</h1>
        <table class="table is-fullwidth">
            <thead>
                <tr>
                    <th>이름</th>
                    <th>점수</th>
                    <th>달성시간</th>
                </tr>
            </thead>
            <tbody>
                {#each rank_list as rank, i}
                    <tr>
                        <td class="name">
                            <span class="tag is-black is-large rank">{i + 1}등</span>
                            <span class="name">{rank.name}</span>
                        </td>
                        <td>{rank.score}점</td>
                        <td>{new Date(rank.created_at * 1000).toLocaleTimeString()}</td>
                    </tr>
                {/each}
            </tbody>
        </table>
    </div>
</div>

<style>
    table {
        table-layout: fixed;
    }

    th,
    td:not(.name) {
        text-align: center;
    }

    th {
        font-size: 25px;
    }

    td {
        font-size: 22px;
        overflow: hidden;
    }

    .rank {
        width: 75px;
    }

    span.name {
        display: inline-block;
        max-width: calc(100% - 90px);
    }

    tbody tr:nth-child(1) .rank {
        color: #000;
        background-color: #ffd700;
    }

    tbody tr:nth-child(2) .rank {
        color: #000;
        background-color: #c0c0c0;
    }

    tbody tr:nth-child(3) .rank {
        color: #000;
        background-color: #cd7f32;
    }
</style>
