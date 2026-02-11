$files = Get-ChildItem -Path "c:\Users\GC VENTURE\Desktop\impact\dist\dist\html-version" -Filter *.php -Recurse

foreach ($file in $files) {
    # Skip the component files themselves if they are in the list (though we filter by *.php in root mostly, recurse will find components)
    if ($file.FullName -like "*\components\*") { continue }

    $content = Get-Content -Path $file.FullName -Raw

    $originalContent = $content

    # 1. Replace Header Placeholder
    # Using regex to handle potential whitespace or variations
    $content = $content -replace '<div\s+id=["'']header-placeholder["'']>\s*</div>', '<?php include "components/header.php"; ?>'
    
    # 2. Replace Footer Placeholder
    $content = $content -replace '<div\s+id=["'']footer-placeholder["'']>\s*</div>', '<?php include "components/footer.php"; ?>'
    
    # 3. Remove main.js script tag
    # Pattern: <script src="assets/js/main.js"></script>
    $content = $content -replace '<script\s+src=["'']assets/js/main\.js["'']>\s*</script>', ''
    
    # 4. Remove header-loader.js script tag (cleanup)
    $content = $content -replace '<script\s+src=["'']assets/js/header-loader\.js["'']>\s*</script>', ''

    if ($content -ne $originalContent) {
        Set-Content -Path $file.FullName -Value $content -NoNewline
        Write-Host "Updated $($file.Name)"
    }
}
