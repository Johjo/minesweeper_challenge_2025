namespace ChallengeMinesweeper;

// Transformation : Code qui ne renvoit rien à un code qui renvoie une constante (fausse)

public class TestMineSweeper0408
{
    [SetUp]
    public void Setup()
    {
    }
    
    [Test]
    public void Test1()
    {
        Assert.That(minesweeper(), Is.EqualTo("0"));
    }

    private String minesweeper()
    {
        return "0";
    }
}