namespace ChallengeMinesweeper;
/* Observation :
     String lengths are both 2. Strings differ at index 0.
  Expected: "00"
  But was:  "**"

 */

/* Action
 Je constate que solveCell ne fait pas ce que j'attends. Ce qu'il se passe, c'est que je ne regarde pas
 le contenu du cellule mais celui du champ de mine.
 On va regarder le contenu de la cellule
*/


public class TestMineSweeper0408Ter
{
    [SetUp]
    public void Setup()
    {
    }

    [TestCase("", "")]
    [TestCase(".", "0")]
    [TestCase("*", "*")]
    [TestCase("**", "**")]
    [TestCase("..", "00")]
    public void Test1(string unsolvedField, string solvedField)
    {
        Assert.That(Minesweeper(unsolvedField), Is.EqualTo(solvedField));
    }

    private string Minesweeper(string unsolvedField)
    {
        if (unsolvedField == "") 
            return "";

        if (unsolvedField == "**")
            return "**";

        if (unsolvedField == "..")
            return SolveCell(unsolvedField) + SolveCell(unsolvedField);
        
        return SolveCell(unsolvedField);
    }

    private static string SolveCell(string unsolvedField)
    {
        if (unsolvedField[0] == ".")
            return "0";
        return "*";
    }
}