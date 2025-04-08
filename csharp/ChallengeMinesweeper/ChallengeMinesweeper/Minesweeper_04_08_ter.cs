namespace ChallengeMinesweeper;
/* Observation :
Le nombre de fois que je fais un solve cell semble dépendre du nombre de cellule
 */

/* Action
Je vais mettre cela en évidence
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

        if (unsolvedField.Length == 2)
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