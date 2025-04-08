namespace ChallengeMinesweeper;
/* Observation :
C:\Projets\dojo-ytreza-dev\minesweeper_challenge_2025\csharp\ChallengeMinesweeper\ChallengeMinesweeper\Minesweeper_04_08_ter.cs(36,29): error CS1002: ; attendu [C:\Projets\dojo-yt
reza-dev\minesweeper_challenge_2025\csharp\ChallengeMinesweeper\ChallengeMinesweeper\ChallengeMinesweeper.csproj]
 */

/* Action
Il me manque un point virgule 
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
        var solvedField = "";
        
        if (unsolvedField == "")
        {
            solvedField = "";
            return solvedField;
        }

        if (unsolvedField.Length == 2)
        {
             solvedField = SolveCell(unsolvedField) + SolveCell(unsolvedField);
            return solvedField;
        }

        solvedField = SolveCell(unsolvedField);
        return solvedField;
        
    }

    private static string SolveCell(string unsolvedField)
    {
        if (unsolvedField[0] == '.')
            return "0";
        return "*";
    }
}