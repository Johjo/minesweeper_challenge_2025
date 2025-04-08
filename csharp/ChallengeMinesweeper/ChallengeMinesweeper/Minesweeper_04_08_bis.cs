namespace ChallengeMinesweeper;

// Transformations : 
// (unconditional->if) splitting the execution path
// (constant->constant+) a simple constant to a more complex constant

public class TestMineSweeper0408Bis
{
    [SetUp]
    public void Setup()
    {
    }
    
    [TestCase("" ,"")]
    [TestCase("*" ,"*")]
    [TestCase("." ,"0")]
    public void Test1(string unsolvedField, string solvedField)
    {
        Assert.That(minesweeper(unsolvedField), Is.EqualTo(solvedField));
    }

    private string minesweeper(string unsolvedField)
    {
        if (unsolvedField == "")
            return "";
        if (unsolvedField == ".")
            return "0";
        return "*";
    }
}