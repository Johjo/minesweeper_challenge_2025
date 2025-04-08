namespace ChallengeMinesweeper;
/* Observation :
  Message d'erreur :
     Expected string length 3 but was 2. Strings differ at index 2.
  Expected: "000"
  But was:  "00"
  -------------^

 */

/* Action
    je vais rajouter une nouvelle ligne
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
    [TestCase("...", "000")]
    public void Test1(string unsolvedField, string solvedField)
    {
        Assert.That(Minesweeper(unsolvedField), Is.EqualTo(solvedField));
    }

    private string Minesweeper(string unsolvedField)
    {
        var solvedField = "";

        if (unsolvedField.Length >= 1)
            solvedField += SolveCell(unsolvedField);

        if (unsolvedField.Length >= 2)
        {
            solvedField += SolveCell(unsolvedField);
        }
        
        if (unsolvedField.Length >= 3)
        {
            solvedField += SolveCell(unsolvedField);
        }

        return solvedField;
    }

    private static string SolveCell(string unsolvedField)
    {
        if (unsolvedField[0] == '.')
            return "0";
        return "*";
    }
}