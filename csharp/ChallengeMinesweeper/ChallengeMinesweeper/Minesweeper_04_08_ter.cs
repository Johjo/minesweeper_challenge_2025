namespace ChallengeMinesweeper;
/* Observation :
je n'ai toujours pas mis en évidence la duplication de construction d'un champ résolu
 */

/* Action

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
        

        if (unsolvedField.Length == 2)
        {
             solvedField = SolveCell(unsolvedField) + SolveCell(unsolvedField);
        }

        if (unsolvedField.Length == 1)
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