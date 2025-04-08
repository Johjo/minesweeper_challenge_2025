namespace ChallengeMinesweeper;
/* Observation :
C:\Projets\dojo-ytreza-dev\minesweeper_challenge_2025\csharp\ChallengeMinesweeper\ChallengeMinesweeper\Minesweeper_04_08_ter.cs(49,13): error CS0019: Impossible d'appliquer l'opér
ateur '==' aux opérandes de type 'char' et 'string' [C:\Projets\dojo-ytreza-dev\minesweeper_challenge_2025\csharp\ChallengeMinesweeper\ChallengeMinesweeper\ChallengeMinesweeper.cs 
proj]

 */

/* Action
Je dois comparer un char avec un char

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
        if (unsolvedField[0] == '.')
            return "0";
        return "*";
    }
}