# BestPositionsFM

#### Have you ever trained a player out of his natural position and don't know what to expect?  
As a Football Manager player, you might already know that the *STARS DO LIE!* But guess what, **NUMBERS DONT**. This program helps you solve this situation by providing you a list of the best roles and duties for the selected squad (or fully scouted) player. 

### Overview
Although it is clear from the attributes screen which position is the best for the player, if you're someone like me who admires the beauty of data and boundless other possibilities, you're at the right place! This program will help you analyse the player's full capability in **ALL** positions, roles and duties available in the game!

### Insight
A player whose all attributes are known, *i.e. 90+ knowledge level of the player or a squad player* is required to run this program. The program might be developed to predict the best positions for players whose knowledge is not complete, in the future.  

The algorithm is set up in such a way that "key" attributes related to a player's position and role are prioritised. The value of the "secondary" attributes is *no less than 80% of its initial value.*

### Usage
- While in the game, go to a player's default attributes view 
- `cmd/ctrl` + `P` and save it as `Text File` into (this) `/players` folder
- run the python `main.py` script and enter the *name of saved the file*
- the program will showcase the best list of positions, roles and duties for the player, with an *aggregate score* 

### Version History
- <strong>v0.2 (Current)</strong> <br />
    &#9989; Feature Upgrade: <em>Now you can select <strong>only</strong> Attack/Support/Defend duties from the list!</em> <br />

- <strong>v0.1</strong> <br />
    &#9989; Feature Upgrade: <em>Best Positions for now available for Squad Players!</em> <br />
    &#9989; Roles & Duties Added 
    <table>
        <tr><td>Inverted Winger</td><td>Inside Forward</td><td>Winger</td><td>Wide Target Man</td><td>Trequartista</td></tr>
        <tr><td>Raumdeuter</td><td>Mezzala</td><td>Deep Lying</td><td>Central Midfielder</td><td>Box To Box MD</td></tr>
        <tr><td>Carrilero</td><td>Ball Winning MD</td><td>Roaming Playmaker</td><td>Target Man</td><td>Poacher</td></tr>
        <tr><td>Pressing Fwd</td><td>Advanced Forward</td><td>Deep Lying Fwd</td><td>Complete Forward</td><td>False Nine</td></tr>
        <tr><td>Wing Back</td><td>Full Back</td><td>No-Nonsense FB</td><td>Complete WB</td><td>Inverted WB</td></tr>
    </table>
    </details>


- <strong>Initial Commit</strong> <br />
    &#9989; Roles & Duties Added
    <table>
        <tr><td>Attacking Midfielder</td><td>Advanced Playmaker</td><td>Shadow Striker</td><td>Trequartista</td><td>Enganche</td></tr>
    </table>
<!-- ![MIT License](https://img.shields.io/badge/license-MIT-brightgreen) -->
