namespace ChallengeMinesweeper;
/* Observation :
C:\Projets\dojo-ytreza-dev\minesweeper_challenge_2025\csharp\ChallengeMinesweeper\ChallengeMinesweeper\Minesweeper_04_08_ter.cs(38,17): error CS0136: Impossible de déclarer une va 
riable locale ou un paramètre nommé 'solvedField' dans cette portée, car ce nom est utilisé dans une portée locale englobante pour définir une variable locale ou un paramètre [C:\ 
Projets\dojo-ytreza-dev\minesweeper_challenge_2025\csharp\ChallengeMinesweeper\ChallengeMinesweeper\ChallengeMinesweeper.csproj]
 */

/* Action
Je vais déclarer solvedField globalement 
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
            solvedField = ""
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